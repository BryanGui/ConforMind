"""
FILE UTILS - Gestion des chemins de stockage ConforMind-AI SaaS

Fonctions utilitaires pour gérer les fichiers et dossiers multi-clients :
- Architecture SaaS avec isolation par client_id
- Génération chemins de stockage organisés par client/model_id
- Création/suppression dossiers automatique
- Support pour tous types de fichiers (modèles, datasets, rapports)
"""

import os
import shutil
from pathlib import Path
from typing import Optional, Dict, Any, List
from datetime import datetime, timezone

# Configuration des chemins de base (architecture SaaS multi-clients)
BASE_DATA_DIR = Path("data")
CLIENTS_DIR = BASE_DATA_DIR / "clients"

def get_client_base_dir(client_id: str) -> Path:
    """Retourne le répertoire de base pour un client spécifique"""
    return CLIENTS_DIR / client_id

def get_model_file_path(client_id: str, model_id: str, filename: str) -> str:
    """
    Génère le chemin complet pour un fichier modèle (.pkl, .h5, .pt, etc.)
    
    Args:
        client_id: ID unique du client/organisation
        model_id: ID unique du modèle
        filename: Nom du fichier modèle
        
    Returns:
        Chemin complet vers le fichier modèle
        
    Example:
        get_model_file_path("org_123", "abc123", "model.pkl") 
        -> "data/clients/org_123/models/abc123/model.pkl"
    """
    client_dir = get_client_base_dir(client_id)
    model_storage_path = client_dir / "models" / model_id
    return str(model_storage_path / filename)

def get_documentation_path(client_id: str, model_id: str, filename: str) -> str:
    """
    Génère le chemin complet pour la documentation d'un modèle
    
    Args:
        client_id: ID unique du client/organisation
        model_id: ID unique du modèle
        filename: Nom du fichier de documentation
        
    Returns:
        Chemin complet vers le fichier de documentation
    """
    client_dir = get_client_base_dir(client_id)
    doc_storage_path = client_dir / "uploads" / model_id / "docs"
    return str(doc_storage_path / filename)

def get_test_data_path(client_id: str, model_id: str, filename: str) -> str:
    """
    Génère le chemin pour les données de test/validation (CSV, etc.)
    
    Args:
        client_id: ID unique du client/organisation
        model_id: ID unique du modèle
        filename: Nom du fichier de données
        
    Returns:
        Chemin complet vers le fichier de données
    """
    client_dir = get_client_base_dir(client_id)
    data_storage_path = client_dir / "datasets" / model_id
    return str(data_storage_path / filename)

def get_test_results_path(client_id: str, model_id: str, filename: str) -> str:
    """
    Génère le chemin pour les résultats de tests de conformité
    
    Args:
        client_id: ID unique du client/organisation
        model_id: ID unique du modèle
        filename: Nom du fichier de résultats
        
    Returns:
        Chemin complet vers le fichier de résultats
    """
    client_dir = get_client_base_dir(client_id)
    results_storage_path = client_dir / "temp_files" / "test_results" / model_id
    return str(results_storage_path / filename)

def get_report_path(client_id: str, model_id: str, report_type: str = "compliance", timestamp: Optional[str] = None) -> str:
    """
    Génère le chemin pour les rapports PDF générés
    
    Args:
        client_id: ID unique du client/organisation
        model_id: ID unique du modèle
        report_type: Type de rapport (compliance, bias_analysis, full_audit, etc.)
        timestamp: Timestamp optionnel (généré automatiquement si None)
        
    Returns:
        Chemin complet vers le fichier PDF de rapport
        
    Example:
        get_report_path("org_123", "abc123", "compliance") 
        -> "data/clients/org_123/reports/abc123/compliance_report_20250701_143022.pdf"
    """
    if timestamp is None:
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    
    filename = f"{report_type}_report_{timestamp}.pdf"
    client_dir = get_client_base_dir(client_id)
    report_storage_path = client_dir / "reports" / model_id
    return str(report_storage_path / filename)

def create_model_storage_directories(client_id: str, model_id: str) -> None:
    """
    Crée tous les dossiers de stockage nécessaires pour un modèle spécifique d'un client
    
    Args:
        client_id: ID unique du client/organisation
        model_id: ID unique du modèle
        
    Creates:
        - data/clients/{client_id}/models/{model_id}/
        - data/clients/{client_id}/uploads/{model_id}/docs/
        - data/clients/{client_id}/datasets/{model_id}/
        - data/clients/{client_id}/temp_files/test_results/{model_id}/
        - data/clients/{client_id}/reports/{model_id}/
    """
    client_dir = get_client_base_dir(client_id)
    
    directories = [
        client_dir / "models" / model_id,
        client_dir / "uploads" / model_id / "docs",
        client_dir / "datasets" / model_id,
        client_dir / "temp_files" / "test_results" / model_id,
        client_dir / "reports" / model_id
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    print(f"✅ Dossiers créés pour le modèle {model_id} du client {client_id}")

def initialize_storage_structure() -> None:
    """
    Crée la structure de dossiers de base du projet SaaS
    """
    # Créer le dossier clients principal
    os.makedirs(CLIENTS_DIR, exist_ok=True)
    
    print("✅ Structure de stockage SaaS initialisée")
    print(f"📁 Dossier base clients: {CLIENTS_DIR}")

def cleanup_model_files(client_id: str, model_id: str) -> None:
    """
    Supprime tous les fichiers et dossiers associés à un modèle d'un client
    ATTENTION: Opération irréversible !
    
    Args:
        client_id: ID unique du client/organisation
        model_id: ID unique du modèle à nettoyer
    """
    client_dir = get_client_base_dir(client_id)
    
    directories_to_remove = [
        client_dir / "models" / model_id,
        client_dir / "uploads" / model_id,
        client_dir / "datasets" / model_id,
        client_dir / "temp_files" / "test_results" / model_id,
        client_dir / "reports" / model_id
    ]
    
    removed_count = 0
    for directory in directories_to_remove:
        if directory.exists():
            shutil.rmtree(directory)
            removed_count += 1
    
    print(f"✅ {removed_count} dossiers supprimés pour le modèle {model_id} du client {client_id}")

def cleanup_client_files(client_id: str) -> None:
    """
    Supprime TOUS les fichiers d'un client
    ATTENTION: Opération irréversible !
    
    Args:
        client_id: ID unique du client/organisation
    """
    client_dir = get_client_base_dir(client_id)
    
    if client_dir.exists():
        shutil.rmtree(client_dir)
        print(f"✅ Tous les fichiers supprimés pour le client {client_id}")
    else:
        print(f"⚠️  Aucun fichier trouvé pour le client {client_id}")

def get_model_storage_info(client_id: str, model_id: str) -> Dict[str, Any]:
    """
    Retourne des informations sur le stockage d'un modèle d'un client
    
    Args:
        client_id: ID unique du client/organisation
        model_id: ID unique du modèle
        
    Returns:
        Dictionnaire avec les infos de stockage
    """
    client_dir = get_client_base_dir(client_id)
    
    directories = {
        "models": client_dir / "models" / model_id,
        "uploads": client_dir / "uploads" / model_id,
        "datasets": client_dir / "datasets" / model_id,
        "test_results": client_dir / "temp_files" / "test_results" / model_id,
        "reports": client_dir / "reports" / model_id
    }
    
    info:Dict[str, Any] = {
        "client_id": client_id,
        "model_id": model_id,
        "directories": {},
        "total_size_mb": 0.0
    }
    
    for name, path in directories.items():
        exists = path.exists()
        size_mb = 0.0
        file_count = 0
        
        if exists:
            # Calculer la taille totale du dossier
            for file_path in path.rglob("*"):
                if file_path.is_file():
                    size_mb += file_path.stat().st_size / (1024 * 1024)
                    file_count += 1
        
        info["directories"][name] = {
            "path": str(path),
            "exists": exists,
            "size_mb": round(size_mb, 2),
            "file_count": file_count
        }
        
        info["total_size_mb"] += size_mb
    
    info["total_size_mb"] = round(info["total_size_mb"], 2)
    return info

def get_client_storage_info(client_id: str) -> Dict[str, Any]:
    """
    Retourne des informations sur le stockage global d'un client
    
    Args:
        client_id: ID unique du client/organisation
        
    Returns:
        Dictionnaire avec les infos de stockage du client
    """
    client_dir = get_client_base_dir(client_id)
    
    if not client_dir.exists():
        return {
            "client_id": client_id,
            "exists": False,
            "total_size_mb": 0.0,
            "model_count": 0,
            "models": []
        }
    
    # Compter les modèles
    models_dir = client_dir / "models"
    model_ids = []
    if models_dir.exists():
        model_ids = [item.name for item in models_dir.iterdir() if item.is_dir()]
    
    # Calculer la taille totale
    total_size_mb = 0.0
    for file_path in client_dir.rglob("*"):
        if file_path.is_file():
            total_size_mb += file_path.stat().st_size / (1024 * 1024)
    
    return {
        "client_id": client_id,
        "exists": True,
        "total_size_mb": round(total_size_mb, 2),
        "model_count": len(model_ids),
        "models": model_ids
    }

def list_all_clients() -> List[str]:
    """
    Liste tous les clients qui ont des fichiers stockés
    
    Returns:
        Liste des client_ids qui ont des dossiers créés
    """
    if not CLIENTS_DIR.exists():
        return []
    
    client_ids:List[Any] = []
    for item in CLIENTS_DIR.iterdir():
        if item.is_dir():
            client_ids.append(item.name)
    
    return sorted(client_ids)

def list_client_models(client_id: str) -> List[str]:
    """
    Liste tous les modèles d'un client spécifique
    
    Args:
        client_id: ID unique du client/organisation
        
    Returns:
        Liste des model_ids du client
    """
    client_dir = get_client_base_dir(client_id)
    models_dir = client_dir / "models"
    
    if not models_dir.exists():
        return []
    
    model_ids:List[Any] = []
    for item in models_dir.iterdir():
        if item.is_dir():
            model_ids.append(item.name)
    
    return sorted(model_ids)