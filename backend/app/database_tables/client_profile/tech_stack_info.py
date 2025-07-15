"""
CLIENT TECH STACK INFO - Table 4/6

Informations sur l'infrastructure technique et les systèmes du client.
Focus sur les éléments qui impactent la conformité EU AI Act.
"""

from sqlalchemy import Column, String, DateTime, Boolean
from datetime import datetime, timezone

# Import de la base existante
from ..models import Base
#from ..enums import InfrastructureType, CloudProvider, ERPSystem

class ClientTechStackInfo(Base):
    """
    Table 4/6 - Infrastructure technique du client
    
    Focus sur :
    - Infrastructure IT (cloud, on-premise)
    - Systèmes d'entreprise (ERP, CRM)
    - Sécurité et gouvernance des données
    """
    __tablename__ = "client_tech_stack_info"
    
    # ==================== CLÉ PRIMAIRE ====================
    company_id = Column(String, primary_key=True)
    
    # ==================== INFRASTRUCTURE IT ====================
    # Type d'infrastructure principal
    infrastructure_type = Column(String, nullable=True)         # Enum InfrastructureType: "on_premise", "cloud_public", "hybrid"
    
    # Fournisseur cloud principal (si applicable)
    primary_cloud_provider = Column(String, nullable=True)      # Enum CloudProvider: "aws", "azure", "gcp", "ovh"
    cloud_regions = Column(String, nullable=True)               # JSON string: ["eu-west-1", "eu-central-1"]
    
    # Multi-cloud ?
    uses_multiple_clouds = Column(Boolean, default=False)
    secondary_cloud_provider = Column(String, nullable=True)
    
    # ==================== SYSTÈMES D'ENTREPRISE ====================
    # ERP principal
    primary_erp_system = Column(String, nullable=True)          # Enum ERPSystem: "sap", "oracle", "microsoft_dynamics"
    erp_version = Column(String, nullable=True)                 # Version du système ERP
    
    # CRM principal
    primary_crm_system = Column(String, nullable=True)          # "salesforce", "hubspot", "microsoft_dynamics", "custom"
    
    # Autres systèmes importants
    has_data_warehouse = Column(Boolean, default=False)
    data_warehouse_type = Column(String, nullable=True)         # "snowflake", "redshift", "bigquery", "synapse"
    
    # ==================== SÉCURITÉ ET GOUVERNANCE ====================
    # Sécurité des données
    has_data_encryption = Column(Boolean, default=False)
    uses_data_classification = Column(Boolean, default=False)
    has_access_controls = Column(Boolean, default=False)
    
    # Backup et disaster recovery
    has_backup_strategy = Column(Boolean, default=False)
    has_disaster_recovery = Column(Boolean, default=False)
    
    # Localisation des données (important EU AI Act)
    data_residency_eu = Column(Boolean, default=False)          # Données stockées en EU
    data_residency_countries = Column(String, nullable=True)    # JSON: ["france", "germany"]
    
    # ==================== MATURITÉ TECHNIQUE ====================
    # Niveau de maturité IT
    it_maturity_level = Column(String, nullable=True)           # "advanced", "intermediate", "basic"
    
    # Équipe IT
    has_dedicated_it_team = Column(Boolean, default=False)
    it_team_size = Column(String, nullable=True)                # "1-5", "6-20", "20+"
    
    # Support externe
    uses_it_consultants = Column(Boolean, default=False)
    main_it_partner = Column(String, nullable=True)             # Nom du partenaire IT principal
    
    # ==================== MÉTADONNÉES ====================
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f"<ClientTechStackInfo(company_id='{self.company_id}', infrastructure='{self.infrastructure_type}')>"