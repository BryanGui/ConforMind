from enum import Enum

"""
ENUMS pour governance_info.py
"""

# ==================== RESSOURCES HUMAINES ====================

class ComplianceOfficerType(str, Enum):
    DEDICATED_TEAM = "dedicated_team"       # Équipe dédiée
    FULL_TIME = "full_time"                 # Temps plein
    PART_TIME = "part_time"                 # Temps partiel
    NONE = "none"                           # Aucun

class DPOType(str, Enum):
    INTERNAL = "internal"                   # DPO interne
    EXTERNAL = "external"                   # DPO externe
    SHARED = "shared"                       # DPO mutualisé
    NONE = "none"                           # Pas de DPO

class RiskManagementStructure(str, Enum):
    DEDICATED_TEAM = "dedicated_team"       # Équipe dédiée
    INTEGRATED = "integrated"               # Intégré dans équipes
    OUTSOURCED = "outsourced"              # Externalisé
    NONE = "none"                          # Aucune structure

# ==================== BUDGET & ÉQUIPES IT ====================

class ITBudgetRange(str, Enum):
    MICRO = "< 50K€"                       # Micro budget IT
    SMALL = "50K-200K€"                    # Petit budget
    MEDIUM = "200K-500K€"                  # Budget moyen
    LARGE = "500K-1M€"                     # Gros budget
    ENTERPRISE = "> 1M€"                   # Budget entreprise
    NOT_DISCLOSED = "Non communiqué"       # Non communiqué

class ITTeamSize(str, Enum):
    SOLO = "1 personne"                    # IT solo
    SMALL_TEAM = "2-5 personnes"          # Petite équipe
    MEDIUM_TEAM = "6-15 personnes"        # Équipe moyenne
    LARGE_TEAM = "16+ personnes"          # Grande équipe IT
    OUTSOURCED = "Externalisé"            # Pas d'équipe interne

# ==================== GOUVERNANCE IA ====================

class AIGovernanceOwner(str, Enum):
    CEO = "ceo"                            # Direction générale
    CTO = "cto"                            # Direction technique
    DPO = "dpo"                            # Data Protection Officer
    RISK_MANAGER = "risk_manager"          # Risk Manager
    DEDICATED_AI_TEAM = "dedicated_ai_team" # Équipe IA dédiée
    NOBODY = "nobody"                      # Personne

class AIPolicyStatus(str, Enum):
    FORMALIZED = "formalized"              # Politique formalisée
    IN_DEVELOPMENT = "in_development"      # En développement
    PLANNED = "planned"                    # Planifiée
    NONE = "none"                          # Aucune

class AIOverSightProcesses(str, Enum):
    SYSTEMATIC = "systematic"              # Supervision systématique
    AD_HOC = "ad_hoc"                     # Supervision ponctuelle
    NONE = "none"                         # Aucune supervision

# ==================== POLITIQUES & FRAMEWORKS ====================

class DataGovernanceMaturity(str, Enum):
    ADVANCED = "advanced"                  # Maturité avancée
    INTERMEDIATE = "intermediate"          # Maturité intermédiaire
    BASIC = "basic"                       # Maturité basique
    NONE = "none"                         # Aucune gouvernance

class DataGovernanceFramework(str, Enum):
    DAMA_DMBOK = "dama_dmbok"             # DAMA-DMBOK
    DCAM = "dcam"                         # Data Management Capability Assessment Model
    CUSTOM = "custom"                     # Framework personnalisé
    NONE = "none"                         # Aucun framework

class RiskFrameworkType(str, Enum):
    ISO_31000 = "iso_31000"               # ISO 31000
    COSO = "coso"                         # COSO Framework
    CUSTOM = "custom"                     # Framework personnalisé
    NONE = "none"                         # Aucun framework

class SecurityPolicyScope(str, Enum):
    COMPREHENSIVE = "comprehensive"        # Politique complète
    BASIC = "basic"                       # Politique basique
    IN_DEVELOPMENT = "in_development"     # En développement
    NONE = "none"                         # Aucune politique

# ==================== MATURITÉ GLOBALE ====================

class ComplianceMaturityLevel(str, Enum):
    ADVANCED = "advanced"                  # Maturité avancée
    INTERMEDIATE = "intermediate"          # Maturité intermédiaire
    BASIC = "basic"                       # Maturité basique
    MINIMAL = "minimal"                   # Maturité minimale

class EUAIActAwareness(str, Enum):
    EXPERT = "expert"                     # Expert
    INTERMEDIATE = "intermediate"          # Intermédiaire
    BASIC = "basic"                       # Basique
    MINIMAL = "minimal"                   # Minimal

class EUAIActPreparationStatus(str, Enum):
    COMPLIANT = "compliant"               # Déjà conforme
    IN_PROGRESS = "in_progress"           # En cours
    PLANNED = "planned"                   # Planifié
    NOT_STARTED = "not_started"          # Pas commencé

# ==================== PRIORITÉS & DÉFIS ====================

class MainComplianceChallenge(str, Enum):
    UNDERSTANDING_REQUIREMENTS = "understanding_requirements"    # Comprendre exigences
    LACK_EXPERTISE = "lack_expertise"                          # Manque expertise
    BUDGET = "budget"                                           # Budget insuffisant
    COORDINATION = "coordination"                               # Coordination équipes
    OTHER = "other"                                            # Autre défi

class EUAIActPriorityLevel(str, Enum):
    CRITICAL = "critical"                 # Priorité critique
    HIGH = "high"                         # Priorité haute
    MEDIUM = "medium"                     # Priorité moyenne
    LOW = "low"                          # Priorité basse

class TargetComplianceTimeline(str, Enum):
    ALREADY_COMPLIANT = "already_compliant"  # Déjà conforme
    SIX_MONTHS = "6_months"                  # 6 mois
    TWELVE_MONTHS = "12_months"              # 12 mois
    EIGHTEEN_MONTHS = "18_months"            # 18 mois
    UNKNOWN = "unknown"                      # Inconnu