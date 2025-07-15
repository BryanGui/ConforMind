"""
MODELS SQLAlchemy - Architecture complète audit EU AI Act

Structure à 4 niveaux:
1. AIModel: métadonnées des modèles IA
2. ModelAudit: audit technique d'UN modèle spécifique
3. WorkflowAudit: audit des processus MLOps/pipelines
4. SystemAudit: audit infrastructure/sécurité
5. OrganizationAudit: audit global entreprise (vue d'ensemble)
"""

from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, Text, JSON, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
import uuid

from .enums import ModelType, Framework, RiskCategory, UseCaseCategory, ComplianceStatus, WorkflowStage

Base = declarative_base()

class AIModel(Base):
    """
    Table principale - métadonnées des modèles IA
    """
    __tablename__ = "ai_models"
    
    # Métadonnées de base
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, default=lambda: f"Model_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}")
    version = Column(String, default="v1.0")
    creator = Column(String, default="Unknown")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    description = Column(Text)
    
    # Caractéristiques techniques
    model_type = Column(Enum(ModelType))
    framework = Column(Enum(Framework))
    architecture = Column(String)
    parameters_count = Column(Integer)
    file_size_mb = Column(Float(precision=2))
    input_format = Column(String)
    output_format = Column(String)
    
    # EU AI Act - Classification
    risk_category = Column(Enum(RiskCategory))
    use_case_category = Column(Enum(UseCaseCategory))
    deployment_context = Column(Text)
    
    # Données d'entraînement (métadonnées de base)
    training_data_source = Column(Text)
    training_data_size = Column(Integer)
    data_collection_period = Column(String)
    
    # Fichiers et stockage
    model_file_path = Column(String)
    documentation_file_path = Column(String)
    
    # Statut général
    compliance_status = Column(Enum(ComplianceStatus), default=ComplianceStatus.PENDING)
    
    # Relations
    model_audits = relationship("ModelAudit", back_populates="model")

class ModelAudit(Base):
    """
    Audit technique d'UN modèle spécifique
    Focus: performance, biais, robustesse du modèle lui-même
    """
    __tablename__ = "model_audits"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    model_id = Column(String, ForeignKey("ai_models.id"))
    evaluation_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    
    # Tests techniques du modèle
    performance_details = Column(JSON)  # {"accuracy": 0.95, "precision": 0.89, ...}
    bias_analysis_details = Column(JSON)  # {"demographic_parity": 0.85, "issues": [...]}
    robustness_details = Column(JSON)  # {"adversarial_test": true, "stress_test": [...]}
    fairness_details = Column(JSON)  # {"protected_groups": [...], "metrics": {...}}
    
    # Données d'entraînement (analyse détaillée)
    data_quality_details = Column(JSON)  # {"completeness": 0.98, "bias_indicators": [...]}
    data_preprocessing_details = Column(JSON)
    
    # Résultats globaux
    overall_model_score = Column(Float(precision=2))  # 0-100
    model_certification_ready = Column(Boolean, default=False)
    model_recommendations = Column(Text)
    
    # Relations
    model = relationship("AIModel", back_populates="model_audits")

class WorkflowAudit(Base):
    """
    Audit des processus MLOps et pipelines
    Focus: gouvernance, traçabilité, processus de développement
    """
    __tablename__ = "workflow_audits"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    workflow_name = Column(String)  # "Training Pipeline", "Deployment Pipeline"
    workflow_stage = Column(Enum(WorkflowStage))  # DEVELOPMENT, TRAINING, VALIDATION, DEPLOYMENT, MONITORING
    evaluation_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    
    # Processus MLOps
    version_control_details = Column(JSON)  # {"git_tracking": true, "model_versioning": [...]}
    data_lineage_details = Column(JSON)  # {"source_tracking": true, "transformations": [...]}
    model_governance_details = Column(JSON)  # {"approval_process": true, "stakeholders": [...]}
    
    # Monitoring et observabilité
    monitoring_details = Column(JSON)  # {"drift_detection": true, "performance_monitoring": [...]}
    logging_details = Column(JSON)  # {"audit_trail": true, "log_retention": [...]}
    
    # Validation et tests
    validation_process_details = Column(JSON)  # {"test_coverage": 0.95, "validation_steps": [...]}
    deployment_process_details = Column(JSON)  # {"rollback_capability": true, "a_b_testing": [...]}
    
    # Résultats
    workflow_compliance_score = Column(Float(precision=1))  # 0-100
    workflow_recommendations = Column(Text)

class SystemAudit(Base):
    """
    Audit infrastructure, sécurité et système
    Focus: cybersécurité, disponibilité, scalabilité
    """
    __tablename__ = "system_audits"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    system_name = Column(String)  # "Production Environment", "Training Infrastructure"
    evaluation_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    
    # Sécurité
    cybersecurity_details = Column(JSON)  # {"encryption": true, "access_control": [...]}
    access_control_details = Column(JSON)  # {"authentication": true, "authorization": [...]}
    data_protection_details = Column(JSON)  # {"gdpr_compliance": true, "data_anonymization": [...]}
    
    # Infrastructure
    availability_details = Column(JSON)  # {"uptime": 0.999, "disaster_recovery": [...]}
    scalability_details = Column(JSON)  # {"auto_scaling": true, "load_balancing": [...]}
    performance_details = Column(JSON)  # {"response_time": 100, "throughput": [...]}
    
    # Résultats
    system_compliance_score = Column(Float(precision=2))  # 0-100
    system_recommendations = Column(Text)

class OrganizationAudit(Base):
    """
    Audit global au niveau entreprise
    Focus: gouvernance globale, politique IA, vue d'ensemble
    """
    __tablename__ = "organization_audits"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    organization_name = Column(String)
    evaluation_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    
    # Vue d'ensemble des modèles
    models_inventory = Column(JSON)  # Liste de tous les modèles et leur statut
    high_risk_models_count = Column(Integer)
    compliant_models_percentage = Column(Float(precision=2))
    
    # Gouvernance organisationnelle
    ai_governance_policy = Column(JSON)  # {"policy_exists": true, "review_frequency": [...]}
    risk_management_framework = Column(JSON)  # {"framework_implemented": true, "risk_appetite": [...]}
    human_oversight_processes = Column(JSON)  # {"oversight_roles": [...], "escalation_procedures": [...]}
    
    # Formation et sensibilisation
    staff_training_details = Column(JSON)  # {"ai_ethics_training": true, "compliance_training": [...]}
    documentation_management = Column(JSON)  # {"centralized_docs": true, "version_control": [...]}
    
    # Conformité réglementaire
    eu_ai_act_readiness = Column(JSON)  # {"compliance_level": 0.85, "gaps_identified": [...]}
    other_regulations_compliance = Column(JSON)  # {"gdpr": true, "sector_specific": [...]}
    
    # Résultats globaux
    overall_organization_score = Column(Float(precision=2))  # 0-100
    certification_readiness = Column(Boolean, default=False)
    strategic_recommendations = Column(Text)
    next_review_date = Column(DateTime)