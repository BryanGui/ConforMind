"""
Configuration centrale de l'application ConforMind AI
Gère les variables d'environnement et paramètres globaux
Version typée pour éliminer les warnings Pylance
"""

import os
from typing import Final

class Settings:
    """Classe de configuration principale avec types explicites"""
    
    # Application
    APP_NAME: Final[str] = "ConforMind AI Compliance"
    APP_VERSION: Final[str] = "0.1.0"
    DEBUG: Final[bool] = True
    
    # API
    API_V1_PREFIX: Final[str] = "/api/v1"
    HOST: Final[str] = "localhost"
    PORT: Final[int] = 8000
    
    # Database (SQLite pour le MVP local)
    DATABASE_URL: Final[str] = "sqlite:///./conformind.db"
    
    # File Storage (local pour le MVP)
    UPLOAD_DIR: Final[str] = "./data/uploads"
    REPORTS_DIR: Final[str] = "./data/reports"
    MODELS_DIR: Final[str] = "./data/models"
    
    # EU AI Act Configuration
    EU_AI_ACT_VERSION: Final[str] = "2024"
    HIGH_RISK_THRESHOLD: Final[float] = 0.7
    BIAS_THRESHOLD: Final[float] = 0.05  # 5% max bias autorisé
    
    # Security (pour plus tard)
    SECRET_KEY: Final[str] = "dev-secret-key-change-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: Final[int] = 30
    
    def __init__(self) -> None:
        """Initialise les dossiers nécessaires"""
        os.makedirs(self.UPLOAD_DIR, exist_ok=True)
        os.makedirs(self.REPORTS_DIR, exist_ok=True)
        os.makedirs(self.MODELS_DIR, exist_ok=True)

# Instance globale des settings avec type explicite
settings: Settings = Settings()

# Export explicite pour Pylance
__all__ = ["Settings", "settings"]