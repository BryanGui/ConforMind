"""
CLIENT GOVERNANCE - Table 2/6

Structure de gouvernance et maturité compliance du client.
Organisation interne pour la gestion des risques et de la conformité.
FOCUS: Organisation et politiques (pas d'historique d'audits)
"""

from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy import Enum
from datetime import datetime, timezone

# Import de la base existante
from ...models import Base

# Import des enums locaux
from .enums import (
    ComplianceOfficerType, DPOType, RiskManagementStructure,
    ITBudgetRange, ITTeamSize,
    AIGovernanceOwner, AIPolicyStatus, AIOverSightProcesses,
    DataGovernanceMaturity, DataGovernanceFramework, RiskFrameworkType, SecurityPolicyScope,
    ComplianceMaturityLevel, EUAIActAwareness, EUAIActPreparationStatus,
    MainComplianceChallenge, EUAIActPriorityLevel, TargetComplianceTimeline
)

class ClientGovernance(Base):
    """
    Table 2/6 - Gouvernance et organisation compliance du client
    
    Contient les informations sur :
    - Structure de gouvernance (DPO, compliance officer, etc.)
    - Politiques et frameworks en place
    - Maturité en matière de compliance
    - Budget et ressources dédiées
    - Priorités et défis
    
    NOTE: L'historique des audits est dans client_audit.py
    """
    __tablename__ = "client_governance"
    
    # ==================== CLÉ PRIMAIRE ====================
    company_id = Column(String, primary_key=True)
    
    # ==================== RESSOURCES COMPLIANCE ====================
    # Personnes dédiées compliance
    has_compliance_officer = Column(Boolean, default=False)
    compliance_officer_type = Column(Enum(ComplianceOfficerType), nullable=True)
    
    has_data_protection_officer = Column(Boolean, default=False)
    dpo_type = Column(Enum(DPOType), nullable=True)
    
    has_risk_manager = Column(Boolean, default=False)
    risk_management_structure = Column(Enum(RiskManagementStructure), nullable=True)
    
    # ==================== GOUVERNANCE IA ====================
    # Qui s'occupe de l'IA dans l'entreprise
    ai_governance_owner = Column(Enum(AIGovernanceOwner), nullable=True)
    
    has_ai_governance_policy = Column(Boolean, default=False)
    ai_policy_status = Column(Enum(AIPolicyStatus), nullable=True)
    
    has_ai_ethics_committee = Column(Boolean, default=False)
    ai_oversight_processes = Column(Enum(AIOverSightProcesses), nullable=True)
    
    # ==================== POLITIQUES ET FRAMEWORKS ====================
    # Gouvernance des données
    has_data_governance_policy = Column(Boolean, default=False)
    data_governance_maturity = Column(Enum(DataGovernanceMaturity), nullable=True)
    data_governance_framework = Column(Enum(DataGovernanceFramework), nullable=True)
    
    # Gestion des risques
    has_risk_management_framework = Column(Boolean, default=False)
    risk_framework_type = Column(Enum(RiskFrameworkType), nullable=True)
    
    # Politiques sécurité
    has_information_security_policy = Column(Boolean, default=False)
    security_policy_scope = Column(Enum(SecurityPolicyScope), nullable=True)
    
    # ==================== MATURITÉ GLOBALE ====================
    # Auto-évaluation maturité compliance
    compliance_maturity_level = Column(Enum(ComplianceMaturityLevel), nullable=True)
    
    # Préparation EU AI Act
    eu_ai_act_awareness = Column(Enum(EUAIActAwareness), nullable=True)
    eu_ai_act_preparation_status = Column(Enum(EUAIActPreparationStatus), nullable=True)
    
    # ==================== BUDGET ET RESSOURCES IT ====================
    # Budget IT avec enum
    it_budget_range = Column(Enum(ITBudgetRange), nullable=True)
    
    # Taille équipe IT avec enum  
    it_team_size = Column(Enum(ITTeamSize), nullable=True)
    
    # Ressources externes
    uses_external_consultants = Column(Boolean, default=False)
    consultant_types = Column(String, nullable=True)            # JSON string: ["legal", "technical", "compliance"]
    
    # ==================== PRIORITÉS ET DÉFIS ====================
    # Principal défi compliance
    main_compliance_challenge = Column(Enum(MainComplianceChallenge), nullable=True)
    
    # Priorité EU AI Act
    eu_ai_act_priority_level = Column(Enum(EUAIActPriorityLevel), nullable=True)
    
    # Timeline souhaité conformité
    target_compliance_timeline = Column(Enum(TargetComplianceTimeline), nullable=True)
    
    # ==================== MÉTADONNÉES ====================
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f"<ClientGovernance(company_id='{self.company_id}', maturity='{self.compliance_maturity_level}')>"