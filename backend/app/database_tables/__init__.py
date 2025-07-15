"""
DATABASE TABLES - Exports centralisés

Ce fichier permet d'importer facilement tous les modèles et enums depuis un seul endroit.

Usage:
    from database_tables import AIModel, ModelAudit, ModelType, RiskCategory
    from database_tables import Base  # Pour créer les tables
"""

# Import des modèles SQLAlchemy
from .models import (
    Base,
    AIModel,
    ModelAudit,
    WorkflowAudit,
    SystemAudit,
    OrganizationAudit
)

# Import de la table User
from .user import User

# Import des enums
from .enums import (
    ModelType,
    Framework,
    RiskCategory,
    UseCaseCategory,
    ComplianceStatus,
    AuditType,
    WorkflowStage
)

# Export de tout pour faciliter les imports
__all__ = [
    # Base SQLAlchemy
    "Base",
    
    # Modèles principaux
    "AIModel",
    "ModelAudit", 
    "WorkflowAudit",
    "SystemAudit",
    "OrganizationAudit",
    "User",
    
    # Enums
    "ModelType",
    "Framework", 
    "RiskCategory",
    "UseCaseCategory",
    "ComplianceStatus",
    "AuditType",
    "WorkflowStage"
]