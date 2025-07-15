"""
CLIENT BASIC INFO - Table principale entreprise

Informations administratives et légales complètes de l'entreprise.
Données extraites du Kbis ou saisie manuelle.
"""

from sqlalchemy import Column, String, DateTime, Text, Float, Boolean
from sqlalchemy import Enum
from datetime import datetime, timezone
import uuid

# Import de la base SQLAlchemy (adapter le chemin selon votre structure)
from ...models import Base

# Import des enums locaux
from .enums import CompanySize, AnnualRevenueEur, GeographicalScope

class ClientBasicInfo(Base):
    """
    Table 1/4 - Informations de base entreprise complètes
    
    Contient toutes les informations officielles de l'entreprise :
    - Identité légale (nom, forme juridique, etc.)
    - Adresses (siège social, établissements)
    - Données administratives (Kbis, SIREN, APE, etc.)
    - Informations financières de base (capital, CA)
    - Boolean indicateurs systèmes
    - Modularité multi-solutions
    """
    __tablename__ = "client_basic_info"
    
    # ==================== CLÉ PRIMAIRE ====================
    company_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    
    # ==================== IDENTITÉ LÉGALE ====================
    company_name = Column(String, nullable=False)
    legal_form = Column(String, nullable=True)              # "SA", "SAS", "SARL", "EURL", "SCI"
    trade_name = Column(String, nullable=True)              # Nom commercial (si différent)
    
    # ==================== DONNÉES ADMINISTRATIVES ====================
    siren = Column(String, nullable=True)                   # 9 chiffres (entreprise)
    siret = Column(String, nullable=True)                   # 14 chiffres (établissement)
    kbis_number = Column(String, nullable=True)             # Numéro RCS complet
    ape_code = Column(String, nullable=True)                # Code APE français "6419Z"
    primary_nace_code = Column(String, nullable=True)       # Code NACE européen "64.19"
    primary_nace_description = Column(Text, nullable=True)  # Description activité
    secondary_nace_codes = Column(String, nullable=True)    # JSON string des codes secondaires
    
    # ==================== LOCALISATION ====================
    headquarters_address = Column(Text, nullable=True)      # Adresse complète
    headquarters_city = Column(String, nullable=True)
    headquarters_postal_code = Column(String, nullable=True)
    headquarters_country = Column(String, nullable=False)   # "France", "Germany", etc.
    geographical_scope = Column(Enum(GeographicalScope), default=GeographicalScope.EU_ONLY)
    
    # ==================== TAILLE ENTREPRISE ====================
    company_size = Column(Enum(CompanySize), nullable=False)
    annual_revenue_eur = Column(Enum(AnnualRevenueEur), nullable=False)
    share_capital_eur = Column(Float, nullable=True)        # Capital social en euros
    creation_date = Column(DateTime, nullable=True)         # Date de création société
    
    # ==================== CONTACT PRINCIPAL ====================
    main_email = Column(String, nullable=True)              # Email général entreprise
    main_phone = Column(String, nullable=True)              # Téléphone principal
    website_url = Column(String, nullable=True)             # Site web
    
    # ==================== BOOLEAN INDICATEURS SYSTÈMES ====================
    has_erp_system = Column(Boolean, nullable=True)         # A-t-il un ERP ?
    has_crm_system = Column(Boolean, nullable=True)         # A-t-il un CRM ?
    has_cloud_infrastructure = Column(Boolean, nullable=True) # Infrastructure cloud ?
    has_data_warehouse = Column(Boolean, nullable=True)     # Entrepôt de données ?
    has_ai_systems = Column(Boolean, nullable=True)         # Systèmes IA déployés ?
    has_compliance_program = Column(Boolean, nullable=True) # Programme compliance ?
    
    # ==================== MODULARITÉ MULTI-SOLUTIONS ====================
    deployment_mode = Column(String, default="saas")        # "saas" | "local" | "hybrid"
    owner_user_id = Column(String, nullable=True)           # Lien vers User qui gère cette entreprise
    
    # ==================== MÉTADONNÉES ====================
    data_source = Column(String, default="manual")          # "manual", "kbis_upload", "api_import"
    kbis_file_path = Column(String, nullable=True)          # Chemin vers Kbis uploadé
    data_verification_status = Column(String, default="pending")  # "pending", "verified", "needs_update"
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f"<ClientBasicInfo(name='{self.company_name}', country='{self.headquarters_country}')>"



