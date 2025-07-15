"""
TECHSTACK INFO - Infrastructure et systèmes techniques

Table unique pour le profil technique d'une entreprise :
- Infrastructure IT (cloud/on-premise/hybride)
- Systèmes d'entreprise (ERP, CRM, etc.)
- Outils de monitoring et sécurité
"""

from sqlalchemy import Column, String, DateTime, Boolean, Text
from sqlalchemy import Enum
from datetime import datetime, timezone

# Import de la base SQLAlchemy
from ...models import Base

# Import des enums locaux
from .enums import InfrastructureType

class ClientTechStack(Base):
    """
    Table profil technique - Infrastructure et systèmes d'une entreprise
    
    Contient vue d'ensemble de l'écosystème technique :
    - Type d'infrastructure et fournisseurs
    - Systèmes d'entreprise principaux
    - Outils de monitoring et sécurité
    """
    __tablename__ = "client_techstack"
    
    # ==================== CLÉ PRIMAIRE ====================
    company_id = Column(String, primary_key=True)
    
    # ==================== INFRASTRUCTURE IT ====================
    infrastructure_type = Column(Enum(InfrastructureType), nullable=False)
    
    # Cloud provider (autocomplete depuis JSON)
    cloud_provider_name = Column(String, nullable=True)
    cloud_regions = Column(String, nullable=True)              # JSON array des régions
    cloud_services_used = Column(Text, nullable=True)          # Services principaux utilisés
    
    # ==================== SYSTÈMES D'ENTREPRISE ====================
    # ERP
    has_erp_system = Column(Boolean, nullable=False)
    erp_system_name = Column(String, nullable=True)            # Autocomplete depuis JSON
    erp_version = Column(String, nullable=True)                # Version/édition
    erp_modules = Column(Text, nullable=True)                  # Modules utilisés
    
    # CRM  
    has_crm_system = Column(Boolean, nullable=False)
    crm_system_name = Column(String, nullable=True)            # Autocomplete depuis JSON
    crm_version = Column(String, nullable=True)
    crm_integrations = Column(Text, nullable=True)             # Intégrations principales
    
    # Data Warehouse / BI
    has_data_warehouse = Column(Boolean, nullable=False)
    data_warehouse_type = Column(String, nullable=True)        # "snowflake", "redshift", etc.
    bi_tools = Column(Text, nullable=True)                     # Tableau, Power BI, etc.
    
    # ==================== DÉVELOPPEMENT & DEVOPS ====================
    has_development_platform = Column(Boolean, nullable=False)
    development_tools = Column(Text, nullable=True)            # JSON array outils dev
    ci_cd_platform = Column(String, nullable=True)             # GitLab, Jenkins, etc.
    version_control = Column(String, nullable=True)            # Git, SVN, etc.
    
    # ==================== MONITORING & OBSERVABILITÉ ====================
    has_monitoring_tools = Column(Boolean, nullable=False)
    monitoring_tools = Column(Text, nullable=True)             # JSON array depuis JSON file
    log_management = Column(String, nullable=True)             # ELK, Splunk, etc.
    apm_tools = Column(String, nullable=True)                  # Datadog, New Relic, etc.
    
    # ==================== SÉCURITÉ ====================
    has_security_tools = Column(Boolean, nullable=False)
    security_tools = Column(Text, nullable=True)               # JSON array outils sécu
    endpoint_protection = Column(String, nullable=True)        # Antivirus, EDR
    network_security = Column(String, nullable=True)           # Firewall, IPS, etc.
    identity_management = Column(String, nullable=True)        # Active Directory, Okta, etc.
    
    # ==================== BACKUP & DISASTER RECOVERY ====================
    has_backup_solution = Column(Boolean, nullable=False)
    backup_solution = Column(String, nullable=True)
    disaster_recovery_plan = Column(Boolean, nullable=False)
    rto_target = Column(String, nullable=True)                 # Recovery Time Objective
    rpo_target = Column(String, nullable=True)                 # Recovery Point Objective
    
    # ==================== MÉTADONNÉES ====================
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f"<ClientTechStack(company_id='{self.company_id}', infrastructure='{self.infrastructure_type.value}')>"