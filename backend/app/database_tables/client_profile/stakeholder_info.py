"""
CLIENT STAKEHOLDER INFO - Table 3/6

Informations essentielles sur les parties prenantes du client.
VERSION SIMPLIFIÉE : Focus sur compliance et contact principal uniquement.
"""

from sqlalchemy import Column, String, DateTime, Boolean
from datetime import datetime, timezone

# Import de la base existante
from ..models import Base

class ClientStakeholderInfo(Base):
    """
    Table 3/6 - Parties prenantes du client (VERSION SIMPLE)
    
    Focus sur :
    1. Comment est gérée leur compliance (qui s'en occupe ?)
    2. Notre contact principal
    """
    __tablename__ = "client_stakeholder_info"
    
    # ==================== CLÉ PRIMAIRE ====================
    company_id = Column(String, primary_key=True)
    
    # ==================== GESTION COMPLIANCE ====================
    # Qui s'occupe de la compliance dans l'entreprise ?
    compliance_owner = Column(String, nullable=True)            # "ceo", "cto", "dpo", "compliance_officer", "legal", "nobody"
    
    # A-t-il des ressources dédiées ?
    has_dedicated_compliance_team = Column(Boolean, default=False)
    has_dpo = Column(Boolean, default=False)
    
    # ==================== CONTACT PRINCIPAL ====================
    # Notre interlocuteur principal
    primary_contact_name = Column(String, nullable=True)
    primary_contact_role = Column(String, nullable=True)        # "ceo", "cto", "dpo", "compliance_officer"
    primary_contact_email = Column(String, nullable=True)
    primary_contact_phone = Column(String, nullable=True)
    
    # ==================== MÉTADONNÉES ====================
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f"<ClientStakeholderInfo(company_id='{self.company_id}', contact='{self.primary_contact_name}')>"