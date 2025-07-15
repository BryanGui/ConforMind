"""
CERTIFICATION INFO - Tables pour gestion des certifications

Table 1: CertificationMaster (référentiel global)
Table 2: ClientCertification (certifications par client)
"""

from sqlalchemy import Column, String, DateTime, Text, Boolean, Integer
from sqlalchemy import Enum
from datetime import datetime, timezone
import uuid

# Import de la base SQLAlchemy
from ...models import Base

# Import des enums locaux
from .enums import CertificationStatus, ComplianceLevel

class CertificationMaster(Base):
    """
    Table référentiel - Toutes les certifications connues
    
    Géré par admin, permet autocomplete et descriptions standardisées.
    Évolutif sans redéploiement.
    """
    __tablename__ = "certifications_master"
    
    # ==================== CLÉ PRIMAIRE ====================
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    
    # ==================== IDENTIFICATION ====================
    code = Column(String, unique=True, nullable=False)      # "iso_27001", "pci_dss"
    name = Column(String, nullable=False)                   # "ISO 27001", "PCI DSS"
    
    # ==================== DESCRIPTIONS 2 NIVEAUX ====================
    short_description = Column(String, nullable=False)      # "Sécurité de l'information"
    long_description = Column(Text, nullable=True)          # Description détaillée complète
    
    # ==================== CATÉGORISATION ====================
    category = Column(String, nullable=False)               # "security", "finance", "ai", "quality"
    sector = Column(String, nullable=True)                  # "banking", "healthcare", "general"
    
    # ==================== MÉTADONNÉES ====================
    is_active = Column(Boolean, default=True)               # Activer/désactiver certification
    popularity_rank = Column(Integer, default=999)          # Pour tri autocomplete (1 = plus populaire)
    
    # ==================== AUDIT ====================
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    created_by = Column(String, nullable=True)              # Admin qui a ajouté
    
    def __repr__(self):
        return f"<CertificationMaster(code='{self.code}', name='{self.name}')>"

class ClientCertification(Base):
    """
    Table certifications clients - Certifications d'une entreprise spécifique
    
    Permet certifications standard (lien master) ET certifications custom.
    Descriptions flexibles selon le contexte.
    """
    __tablename__ = "client_certifications"
    
    # ==================== CLÉ PRIMAIRE ====================
    certification_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    
    # ==================== LIAISON ENTREPRISE ====================
    company_id = Column(String, nullable=False)             # FK vers client_basic_info
    
    # ==================== CERTIFICATION INFO ====================
    certification_name = Column(String, nullable=False)     # Nom saisi (libre ou depuis master)
    certification_master_id = Column(String, nullable=True) # FK vers certifications_master (si standard)
    
    # ==================== DESCRIPTIONS FLEXIBLES ====================
    # Si certification_master_id existe → ces champs optionnels (override possible)
    # Si certification custom → ces champs obligatoires frontend
    description_short = Column(String, nullable=True)       # Description courte custom/override
    description_long = Column(Text, nullable=True)          # Description longue custom/override
    
    # ==================== DÉTAILS CERTIFICATION ====================
    standard_version = Column(String, nullable=True)        # "2022", "v1.3", "Edition 2020"
    certificate_number = Column(String, nullable=True)      # Numéro certificat
    certifying_body = Column(String, nullable=True)         # "AFNOR", "Bureau Veritas", "PwC"
    scope = Column(Text, nullable=True)                     # Périmètre de la certification
    
    # ==================== DATES OBLIGATOIRES ====================
    certification_date = Column(DateTime, nullable=False)   # Date d'obtention
    expiry_date = Column(DateTime, nullable=False)          # Date d'expiration
    
    # ==================== STATUT ET CONFORMITÉ ====================
    status = Column(Enum(CertificationStatus), nullable=False)
    compliance_level = Column(Enum(ComplianceLevel), nullable=True)
    
    # ==================== FICHIERS ====================
    certificate_file_path = Column(String, nullable=True)   # Chemin vers certificat PDF
    
    # ==================== MÉTADONNÉES ====================
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f"<ClientCertification(name='{self.certification_name}', status='{self.status.value}')>"