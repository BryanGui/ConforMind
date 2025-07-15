# routers/health.py
from fastapi import APIRouter
from datetime import datetime
import psutil
import os
import sqlite3
from typing import List

# Import des schémas depuis api_schemas/
from app.api_schemas.health import (
    HealthResponse,
    ComponentStatus,
    DetailedHealthResponse,
    VersionResponse
)

router = APIRouter(prefix="/health", tags=["Health"])

# ==================== ROUTES ====================

@router.get("/", response_model=HealthResponse)
async def basic_health():
    """
    Endpoint de santé basique - retourne toujours OK
    Utilisé par les load balancers et monitoring
    """
    return HealthResponse(
        status="OK",
        timestamp=datetime.now(),
        message="ConforMind-AI API is running"
    )

@router.get("/detailed", response_model=DetailedHealthResponse)
async def detailed_health():
    """
    Santé détaillée avec vérification des composants critiques
    """
    components:List[ComponentStatus] = []
    overall_status = "OK"
    
    # 1. Vérifier Database SQLite
    try:
        start_time = datetime.now()
        # Test simple connexion + requête
        conn = sqlite3.connect("data/conformind.db")
        conn.execute("SELECT 1").fetchone()
        conn.close()
        
        response_time = (datetime.now() - start_time).total_seconds() * 1000
        components.append(ComponentStatus(
            name="SQLite Database",
            status="OK",
            details="Connection successful",
            response_time_ms=round(response_time, 2)
        ))
    except Exception as e:
        overall_status = "ERROR"
        components.append(ComponentStatus(
            name="SQLite Database",
            status="ERROR",
            details=f"Connection failed: {str(e)}"
        ))
    
    # 2. Vérifier Storage (dossier data/)
    try:
        data_dir = "data"
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        
        # Test écriture
        test_file = os.path.join(data_dir, "health_check.tmp")
        with open(test_file, "w") as f:
            f.write("health_check")
        os.remove(test_file)
        
        components.append(ComponentStatus(
            name="File Storage",
            status="OK",
            details=f"Directory {data_dir} is writable"
        ))
    except Exception as e:
        overall_status = "ERROR"
        components.append(ComponentStatus(
            name="File Storage",
            status="ERROR",
            details=f"Storage error: {str(e)}"
        ))
    
    # 3. Vérifier Ressources Système
    try:
        # Récupération des métriques (types corrects)
        memory = psutil.virtual_memory()      # svmem object
        disk = psutil.disk_usage('.')         # sdiskusage object
        cpu_percent: float = psutil.cpu_percent(interval=1)  # direct float
        
        # Extraction des pourcentages
        memory_percent: float = memory.percent
        disk_percent: float = disk.percent
        
        # Logique de statut basée sur TOUS les composants
        resource_status = "OK"
        
        # Seuils CRITIQUES (ERROR)
        if memory_percent > 90 or cpu_percent > 95 or disk_percent > 95:
            resource_status = "ERROR"
            overall_status = "ERROR"
        # Seuils WARNING
        elif memory_percent > 75 or cpu_percent > 80 or disk_percent > 85:
            resource_status = "WARNING"
            overall_status = "WARNING" if overall_status == "OK" else overall_status
        
        components.append(ComponentStatus(
            name="System Resources",
            status=resource_status,
            details=f"RAM: {memory_percent:.1f}%, CPU: {cpu_percent:.1f}%, Disk: {disk_percent:.1f}%"
        ))
        
    except Exception as e:
        components.append(ComponentStatus(
            name="System Resources",
            status="WARNING",
            details=f"Could not read system metrics: {str(e)}"
        ))
    
    return DetailedHealthResponse(
        status=overall_status,
        timestamp=datetime.now(),
        components=components,
        system_info={
            "python_version": f"{psutil.version_info[0]}.{psutil.version_info[1]}.{psutil.version_info[2]}",
            "platform": os.name,
            "process_id": os.getpid()
        }
    )

@router.get("/version", response_model=VersionResponse)
async def api_version():
    """
    Informations version et build de l'API
    """
    # Calcul uptime basique (depuis start du process)
    process = psutil.Process(os.getpid())
    uptime = datetime.now().timestamp() - process.create_time()
    
    return VersionResponse(
        api_version="1.0.0",
        environment="local",  # TODO: Lire depuis config
        build_timestamp=datetime(2025, 1, 1, 12, 0, 0),  # TODO: Real build time
        uptime_seconds=round(uptime, 2)
    )