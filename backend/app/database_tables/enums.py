"""
ENUMS - Valeurs fixes autorisées pour ConforMind-AI

Ce fichier définit des "listes fermées" de valeurs possibles pour certains champs.
Exemple: Un modèle ne peut être QUE "classification" OU "regression" OU "llm", etc.

Avantages:
- Évite les erreurs de frappe
- Crée automatiquement des listes déroulantes dans le frontend
- Validation automatique des données
- Code plus robuste et maintenable
"""
import enum

class ModelType(enum.Enum):
    CLASSIFICATION = "classification"
    REGRESSION = "regression"
    LLM = "llm"
    COMPUTER_VISION = "computer_vision"
    NLP = "nlp"
    MULTIMODAL = "multimodal"

class Framework(enum.Enum):
    TENSORFLOW = "tensorflow"
    PYTORCH = "pytorch"
    SKLEARN = "sklearn"
    HUGGINGFACE = "huggingface"
    ONNX = "onnx"
    CUSTOM = "custom"

class RiskCategory(enum.Enum):
    PROHIBITED = "prohibited"
    HIGH_RISK = "high_risk"
    LIMITED_RISK = "limited_risk"
    MINIMAL_RISK = "minimal_risk"

class UseCaseCategory(enum.Enum):
    RECRUITMENT = "recruitment"
    CREDIT_SCORING = "credit_scoring"
    LAW_ENFORCEMENT = "law_enforcement"
    HEALTHCARE = "healthcare"
    EDUCATION = "education"
    BIOMETRIC = "biometric"
    CONTENT_GENERATION = "content_generation"

class AuditType(enum.Enum):
    MODEL_AUDIT = "model_audit"
    WORKFLOW_AUDIT = "workflow_audit"
    SYSTEM_AUDIT = "system_audit"
    ORGANIZATION_AUDIT = "organization_audit"

class WorkflowStage(enum.Enum):
    DEVELOPMENT = "development"
    TRAINING = "training"
    VALIDATION = "validation"
    DEPLOYMENT = "deployment"
    MONITORING = "monitoring"
    MAINTENANCE = "maintenance"


class CompanySize(enum.Enum):
    """Classification PME selon EU AI Act Article 55 & Recommendation 2003/361/EC"""
    MICRO = "1-9 employés + < 2M€ CA (micro)"      # Allègements max
    SMALL = "10-49 employés + < 10M€ CA (small)"   # Support PME
    MEDIUM = "50-249 employés + < 50M€ CA (medium)" # Support PME  
    LARGE = "250+ employés ou > 50M€ CA (large)"    # Obligations complètes

class AnnualRevenueEur(enum.Enum):
    """Chiffre d'affaires (requis pour classification PME - EU AI Act Art.55)"""
    MICRO = "< 2M€ (micro)"
    SMALL = "2-10M€ (small)"  
    MEDIUM = "10-50M€ (medium)"
    LARGE = "> 50M€ (large)"
    PREFER_NOT_SAY = "Non communiqué"

class GeographicalScope(enum.Enum):
    """Périmètre géographique"""
    EU_ONLY = "eu_only"
    EU_INTERNATIONAL = "eu_international"
    INTERNATIONAL_EU_USERS = "intl_eu_users"


"""
📋 EU AI Act Annex III - Les 8 domaines officiels :

Biometrics ✅
Critical infrastructure ✅
Education and vocational training ✅
Employment, workers management and access to self-employment ✅
Access to and enjoyment of essential private services and essential public services ✅
Law enforcement ✅
Migration, asylum and border control management ✅
Administration of justice and democratic processes ✅

"""

class RiskDomain(enum.Enum):
    """Domaines de risque EU AI Act"""
    BIOMETRICS = "biometrics"
    CRITICAL_INFRASTRUCTURE = "critical_infrastructure"
    EDUCATION = "education"
    EMPLOYMENT = "employment"
    ESSENTIAL_SERVICES = "essential_services"
    LAW_ENFORCEMENT = "law_enforcement"
    MIGRATION_BORDER = "migration_border"
    JUSTICE_DEMOCRACY = "justice_democracy"


class CertificationStatus(enum.Enum):
    """Statut des certifications externes (ISO 27001, SOX, GDPR, etc.)"""
    VALID = "valid"                     # Certification active et valide
    EXPIRED = "expired"                 # Certification expirée  
    IN_PROGRESS = "in_progress"         # En cours d'obtention
    SUSPENDED = "suspended"             # Suspendue temporairement
    REVOKED = "revoked"                 # Révoquée définitivement

class ComplianceStatus(enum.Enum):
    """Statut de conformité EU AI Act (Article 43)"""
    NOT_ASSESSED = "not_assessed"                       # Pas encore évalué
    IN_CONFORMITY_ASSESSMENT = "in_conformity_assessment"  # Audit en cours (terme officiel)
    COMPLIANT = "compliant"                             # ✅ Terme officiel EU AI Act  
    NON_COMPLIANT = "non_compliant"                     # ❌ Terme officiel EU AI Act
    PARTIALLY_COMPLIANT = "partially_compliant"         # Extension logique

class RemediationStatus(enum.Enum):
    NOT_REQUIRED = "not_required"
    NOT_STARTED = "not_started"  
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class ClientStatus(enum.Enum):
    """Statut commercial/business du client"""
    PROSPECT = "prospect"                    # Lead non qualifié
    QUALIFIED_LEAD = "qualified_lead"        # Lead qualifié
    ACTIVE_CLIENT = "active_client"          # Client payant
    CHURNED_CLIENT = "churned_client"        # Client perdu
    BLOCKED_BUDGET = "blocked_budget"        # Veut mais pas de budget
    CANCELLED_PROJECT = "cancelled_project"  # Projet abandonné
    RENEWAL_DUE = "renewal_due"              # Renouvellement approche

class InfrastructureType(enum.Enum):
    """Type d'infrastructure IT"""
    ON_PREMISE = "on_premise"
    CLOUD_PUBLIC = "cloud_public" 
    CLOUD_PRIVATE = "cloud_private"
    HYBRID = "hybrid"

class CloudProvider(enum.Enum):
    """Fournisseurs cloud principaux"""
    AWS = "aws"
    AZURE = "azure"
    GCP = "gcp"
    OVH = "ovh"
    DIGITAL_OCEAN = "digital_ocean"
    OTHER = "other"
    NOT_APPLICABLE = "not_applicable"

class ERPSystem(enum.Enum):
    """Systèmes ERP"""
    SAP = "sap"
    ORACLE = "oracle"
    MICROSOFT_DYNAMICS = "microsoft_dynamics"
    ODOO = "odoo"
    SAGE = "sage"
    CUSTOM = "custom"
    NONE = "none"
    OTHER = "other"

class LLMProvider(enum.Enum):
    """Fournisseurs LLM externes"""
    OPENAI = "openai"               # ChatGPT, GPT-4
    ANTHROPIC = "anthropic"         # Claude
    GOOGLE = "google"               # Gemini, Bard
    MICROSOFT = "microsoft"         # Copilot
    HUGGINGFACE = "huggingface"     # Modèles open source
    COHERE = "cohere"
    MISTRAL = "mistral"
    OTHER = "other"

class AIMaturityLevel(enum.Enum):
    """Niveau de maturité IA de l'entreprise"""
    BEGINNER = "beginner"           # Découverte IA
    INTERMEDIATE = "intermediate"   # Quelques projets
    ADVANCED = "advanced"           # IA généralisée
    EXPERT = "expert"               # Leader IA