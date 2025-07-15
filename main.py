#!/usr/bin/env python3
"""
CONFORMIND-AI - Point d'entrée principal
Configuration pour MVP SaaS avec imports dynamiques
"""

from contextlib import asynccontextmanager
# Imports après configuration du path
import uvicorn 
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

# Import de votre configuration
from app.core.config import settings 
from app.core.database import initialize_database, HealthyDatabase,UnhealthyDatabase, DatabaseHealth
from typing import Union


# Import de tous vos routers
from app.routers.health import router as health_router
from app.routers.ai_models import router as ai_models_router 
from app.routers.compliance import router as compliance_router
from app.routers.reports import router as reports_router


health: Union[HealthyDatabase, UnhealthyDatabase] = initialize_database()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gestion du cycle de vie de l'application"""
    # STARTUP
    print("🚀 Démarrage ConforMind-AI API...")
    
    # Initialiser base de données et stockage
    health: DatabaseHealth = initialize_database()
    
    # Type narrowing avec pattern matching
    if health["status"] == "healthy":
        print("✅ Base de données initialisée")
        print(f"📁 Fichier DB: {health['database_file']}")
    else:
        print(f"❌ Problème DB: {health['error']}")
        print(f"📁 Fichier DB: {health['database_file']}")
    
    print(f"📍 API disponible sur: http://localhost:{settings.PORT}")
    print(f"📚 Documentation: http://localhost:{settings.PORT}/docs")
    
    yield  # L'application tourne ici
    
    # SHUTDOWN (optionnel)
    print("🛑 Arrêt ConforMind-AI API...")


# Création de l'app FastAPI avec lifespan
app = FastAPI(
    title="ConforMind-AI API",
    description="EU AI Act Compliance Automation Platform",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# CORS pour frontend (React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # Vite/React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Enregistrement des routers
app.include_router(health_router)
app.include_router(ai_models_router)
app.include_router(compliance_router)
app.include_router(reports_router)


@app.get("/")
async def root():
    """Page d'accueil API"""
    return {
        "message": "ConforMind-AI API",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs"
    }

if __name__ == "__main__":
    # Configuration développement
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True,  # Auto-reload en dev
        log_level="info"
    )