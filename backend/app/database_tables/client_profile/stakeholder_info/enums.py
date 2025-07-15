"""
ENUMS pour stakeholder_info.py
Gestion des contacts et interlocuteurs d'une entreprise cliente
"""
from enum import Enum

# ==================== ORGANISATION INTERNE ====================

class Department(str, Enum):
    """Départements de l'entreprise"""
    IT = "it"                              # Informatique / Tech
    LEGAL = "legal"                        # Juridique / Conformité
    RISK_MANAGEMENT = "risk_management"    # Gestion des risques
    HUMAN_RESOURCES = "hr"                 # Ressources humaines
    FINANCE = "finance"                    # Finance / Comptabilité
    OPERATIONS = "operations"              # Opérations / Production
    MARKETING = "marketing"                # Marketing / Communication
    SALES = "sales"                        # Commercial / Ventes
    DATA_ANALYTICS = "data_analytics"      # Data / Analytics
    PRODUCT = "product"                    # Product Management
    QUALITY = "quality"                    # Qualité / Audit
    SECURITY = "security"                  # Sécurité / Cybersécurité
    GENERAL_MANAGEMENT = "general_mgmt"    # Direction générale
    OTHER = "other"                        # Autre département

class SeniorityLevel(str, Enum):
    """Niveau hiérarchique dans l'entreprise"""
    C_LEVEL = "c_level"                    # CEO, CTO, CFO, etc.
    EXECUTIVE_DIRECTOR = "exec_director"   # Directeur exécutif
    DIRECTOR = "director"                  # Directeur / VP
    SENIOR_MANAGER = "senior_manager"      # Manager senior
    MANAGER = "manager"                    # Manager / Chef d'équipe
    SENIOR_SPECIALIST = "senior_specialist" # Expert senior
    SPECIALIST = "specialist"              # Spécialiste / Analyste
    JUNIOR = "junior"                      # Junior / Stagiaire
    CONSULTANT = "consultant"              # Consultant externe
    CONTRACTOR = "contractor"              # Prestataire externe

# ==================== RÔLES COMPLIANCE IA ====================

class AIComplianceRole(str, Enum):
    """Rôle dans les projets de conformité IA"""
    DECISION_MAKER = "decision_maker"      # Prend les décisions finales
    PROJECT_SPONSOR = "project_sponsor"    # Sponsor du projet
    VALIDATOR = "validator"                # Valide les livrables
    CONTRIBUTOR = "contributor"            # Contribue activement
    SUBJECT_MATTER_EXPERT = "sme"         # Expert métier
    TECHNICAL_LEAD = "technical_lead"      # Lead technique
    INFORMED = "informed"                  # Informé des avancées
    REVIEWER = "reviewer"                  # Reviewer / Commentateur
    APPROVER = "approver"                  # Approbateur final
    NONE = "none"                          # Pas de rôle spécifique

class ExpertiseDomain(str, Enum):
    """Domaines d'expertise IA et compliance"""
    MACHINE_LEARNING = "machine_learning"           # ML / Data Science
    EU_AI_ACT = "eu_ai_act"                        # Réglementation EU AI Act
    GDPR_PRIVACY = "gdpr_privacy"                  # GDPR / Protection données
    RISK_ASSESSMENT = "risk_assessment"            # Évaluation des risques
    BIAS_FAIRNESS = "bias_fairness"               # Biais / Équité algorithmes
    MODEL_GOVERNANCE = "model_governance"          # Gouvernance modèles IA
    TECHNICAL_DOCUMENTATION = "tech_docs"          # Documentation technique
    AUDIT_COMPLIANCE = "audit_compliance"          # Audit / Conformité
    CYBERSECURITY = "cybersecurity"               # Cybersécurité
    BUSINESS_ANALYSIS = "business_analysis"        # Analyse métier
    PROJECT_MANAGEMENT = "project_management"      # Gestion de projet
    CHANGE_MANAGEMENT = "change_management"        # Conduite du changement
    TRAINING_EDUCATION = "training_education"      # Formation / Éducation
    VENDOR_MANAGEMENT = "vendor_management"        # Gestion fournisseurs
    OTHER = "other"                               # Autre expertise

class InvolvementLevel(str, Enum):
    """Niveau d'implication dans les projets IA"""
    FULL_TIME = "full_time"                # Temps plein dédié
    PART_TIME = "part_time"                # Temps partiel régulier
    OCCASIONAL = "occasional"              # Ponctuel / Au besoin
    CONSULTANT = "consultant"              # Consultant externe
    ADVISORY = "advisory"                  # Rôle consultatif
    MINIMAL = "minimal"                    # Implication minimale

# ==================== AUTORITÉS ET RESPONSABILITÉS ====================

class BudgetAuthorityLevel(str, Enum):
    """Niveau d'autorité budgétaire"""
    FULL_AUTHORITY = "full_authority"      # Autorité budgétaire complète
    LIMITED_AUTHORITY = "limited"          # Autorité limitée (seuils)
    APPROVAL_REQUIRED = "approval_required" # Doit faire approuver
    NONE = "none"                          # Aucune autorité budgétaire

class DecisionScope(str, Enum):
    """Périmètre de décision"""
    STRATEGIC = "strategic"                # Décisions stratégiques
    OPERATIONAL = "operational"            # Décisions opérationnelles
    TECHNICAL = "technical"                # Décisions techniques
    BUDGET = "budget"                      # Décisions budgétaires
    VENDOR_SELECTION = "vendor_selection"  # Sélection fournisseurs
    TIMELINE = "timeline"                  # Décisions calendaires
    SCOPE = "scope"                        # Périmètre projet
    NONE = "none"                         # Aucune décision

# ==================== COMMUNICATION ====================

class PreferredCommunicationMethod(str, Enum):
    """Méthode de communication préférée"""
    EMAIL = "email"                        # Email professionnel
    PHONE = "phone"                        # Téléphone
    VIDEO_CALL = "video_call"             # Visioconférence
    IN_PERSON = "in_person"               # Présentiel
    TEAMS = "teams"                       # Microsoft Teams
    SLACK = "slack"                       # Slack
    WHATSAPP = "whatsapp"                 # WhatsApp Business
    OTHER = "other"                       # Autre méthode

class CommunicationFrequency(str, Enum):
    """Fréquence de communication souhaitée"""
    DAILY = "daily"                       # Quotidienne
    WEEKLY = "weekly"                     # Hebdomadaire
    BIWEEKLY = "biweekly"                # Bimensuelle
    MONTHLY = "monthly"                   # Mensuelle
    QUARTERLY = "quarterly"               # Trimestrielle
    AS_NEEDED = "as_needed"              # Au besoin
    MAJOR_MILESTONES = "major_milestones" # Jalons majeurs seulement

class LanguagePreference(str, Enum):
    """Langue de communication préférée"""
    FRENCH = "fr"                         # Français
    ENGLISH = "en"                        # Anglais
    GERMAN = "de"                         # Allemand
    SPANISH = "es"                        # Espagnol
    ITALIAN = "it"                        # Italien
    DUTCH = "nl"                          # Néerlandais
    OTHER = "other"                       # Autre langue

# ==================== STATUTS ET MÉTADONNÉES ====================

class ContactStatus(str, Enum):
    """Statut du contact"""
    ACTIVE = "active"                     # Contact actif
    INACTIVE = "inactive"                 # Contact inactif
    ON_LEAVE = "on_leave"                # En congé temporaire
    LEFT_COMPANY = "left_company"        # A quitté l'entreprise
    EXTERNAL = "external"                # Contact externe
    PENDING_VALIDATION = "pending"       # En attente de validation

class ContactPriority(str, Enum):
    """Priorité du contact pour les projets"""
    CRITICAL = "critical"                 # Contact critique
    HIGH = "high"                        # Priorité haute
    MEDIUM = "medium"                    # Priorité moyenne
    LOW = "low"                          # Priorité basse
    BACKUP = "backup"                    # Contact de secours

# ==================== TYPES DE CONTRAT ====================

class EmploymentType(str, Enum):
    """Type de contrat de travail"""
    FULL_TIME_EMPLOYEE = "full_time"     # Employé temps plein
    PART_TIME_EMPLOYEE = "part_time"     # Employé temps partiel
    CONTRACTOR = "contractor"            # Contractuel
    CONSULTANT = "consultant"            # Consultant
    INTERN = "intern"                    # Stagiaire
    FREELANCER = "freelancer"           # Freelance
    VENDOR = "vendor"                    # Fournisseur
    PARTNER = "partner"                  # Partenaire
    OTHER = "other"                      # Autre type