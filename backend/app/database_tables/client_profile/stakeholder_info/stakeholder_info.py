"""
CLIENT STAKEHOLDER INFO - Gestion des contacts et interlocuteurs

Table pour stocker tous les contacts d'une entreprise cliente :
- Contacts opérationnels (DPO, CTO, Risk Manager, etc.)
- Informations de contact professionnel
- Rôles dans les projets de conformité IA
- Autorités et responsabilités
- Préférences de communication

RELATION: 1 Company → Many Stakeholders
"""

from sqlalchemy import Column, String, Integer, Boolean, DateTime, Text
from sqlalchemy import Enum, ForeignKey
from datetime import datetime, timezone
import uuid

# Import de la base SQLAlchemy
from ...models import Base

# Import des enums locaux
from .enums import (
    Department, SeniorityLevel, ContactStatus, EmploymentType,
    AIComplianceRole, ExpertiseDomain, InvolvementLevel, DecisionScope,
    PreferredCommunicationMethod, CommunicationFrequency, LanguagePreference,
    ContactPriority, BudgetAuthorityLevel
)

class ClientStakeholder(Base):
    """
    Table contacts/interlocuteurs - Tous les contacts d'une entreprise cliente
    
    Permet de gérer :
    - Contacts multiples par entreprise (relation 1-to-many)
    - Rôles spécifiques dans la conformité IA
    - Autorités et responsabilités détaillées
    - Préférences de communication
    - Suivi de l'activité et disponibilité
    """
    __tablename__ = "client_stakeholders"
    
    # ==================== CLÉ PRIMAIRE ET RELATIONS ====================
    stakeholder_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    company_id = Column(String, ForeignKey("client_basic_info.company_id"), nullable=False)
    
    # ==================== INFORMATIONS PERSONNELLES ====================
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    job_title = Column(String, nullable=False)
    department = Column(Enum(Department), nullable=False)
    seniority_level = Column(Enum(SeniorityLevel), nullable=False)
    employment_type = Column(Enum(EmploymentType), default=EmploymentType.FULL_TIME_EMPLOYEE)
    
    # ==================== CONTACT PROFESSIONNEL ====================
    professional_email = Column(String, nullable=False)
    professional_phone = Column(String, nullable=True)
    office_location = Column(String, nullable=True)        # Texte libre : "Paris La Défense", "Remote", etc.
    linkedin_url = Column(String, nullable=True)
    
    # ==================== RÔLE COMPLIANCE IA ====================
    ai_compliance_role = Column(Enum(AIComplianceRole), nullable=False)
    main_expertise_domain = Column(Enum(ExpertiseDomain), nullable=True)
    additional_expertise_domains = Column(Text, nullable=True)  # JSON
    involvement_level = Column(Enum(InvolvementLevel), nullable=False)
    decision_scope = Column(Enum(DecisionScope), nullable=True)  # Périmètre de décision
    
    # ==================== RESPONSABILITÉS PROJETS ====================
    is_primary_contact = Column(Boolean, nullable=False, default=False)
    can_make_decisions = Column(Boolean, nullable=False, default=False)
    budget_authority_level = Column(Enum(BudgetAuthorityLevel), default=BudgetAuthorityLevel.NONE)
    is_technical_validator = Column(Boolean, nullable=False, default=False)
    is_legal_validator = Column(Boolean, nullable=False, default=False)
    can_sign_contracts = Column(Boolean, nullable=False, default=False)
    
    # ==================== DISPONIBILITÉ ====================
    availability_hours_per_week = Column(Integer, nullable=True)  # Heures/semaine disponibles pour IA
    timezone = Column(String, nullable=True)              # "Europe/Paris", "UTC", etc.
    working_hours = Column(String, nullable=True)         # "9h-18h", "Flexible", etc.
    
    # ==================== PRÉFÉRENCES COMMUNICATION ====================
    preferred_communication_method = Column(Enum(PreferredCommunicationMethod), nullable=False)
    communication_frequency = Column(Enum(CommunicationFrequency), default=CommunicationFrequency.AS_NEEDED)
    language_preference = Column(Enum(LanguagePreference), default=LanguagePreference.FRENCH)
    
    # ==================== GESTION CONTACT ====================
    contact_status = Column(Enum(ContactStatus), nullable=False, default=ContactStatus.ACTIVE)
    contact_priority = Column(Enum(ContactPriority), nullable=False, default=ContactPriority.MEDIUM)
    
    # Dates importantes
    start_date = Column(DateTime, nullable=True)           # Date d'arrivée dans l'entreprise
    end_date = Column(DateTime, nullable=True)             # Date de départ (si applicable)
    last_contact_date = Column(DateTime, nullable=True)    # Dernière interaction
    
    # ==================== NOTES ET MÉTADONNÉES ====================
    notes = Column(Text, nullable=True)                   # Notes libres sur le contact
    internal_notes = Column(Text, nullable=True)          # Notes internes (non visibles client)
    
    # Métadonnées techniques
    created_by = Column(String, nullable=True)            # Qui a créé ce contact
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    # ==================== MÉTADONNÉES ====================
    
    def __repr__(self):
        return f"<ClientStakeholder(name='{self.first_name} {self.last_name}', role='{self.ai_compliance_role.value}', company_id='{self.company_id}')>"