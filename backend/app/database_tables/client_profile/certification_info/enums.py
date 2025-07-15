"""
ENUMS pour certification_info.py
Seulement les valeurs stables (statuts et niveaux)
"""
from enum import Enum

class CertificationStatus(str, Enum):
    """Statut actuel de la certification"""
    VALID = "valid"                            # ✅ Certification active et valide
    EXPIRED = "expired"                        # ❌ Certification expirée
    IN_PROGRESS = "in_progress"                # 🔄 En cours d'obtention
    SUSPENDED = "suspended"                    # ⏸️ Suspendue temporairement
    REVOKED = "revoked"                        # 🚫 Révoquée définitivement
    RENEWAL_REQUIRED = "renewal_required"      # ⚠️ Renouvellement nécessaire
    NOT_APPLICABLE = "not_applicable"          # N/A pour ce type d'entreprise

class ComplianceLevel(str, Enum):
    """Niveau de conformité/couverture"""
    FULL_COMPLIANCE = "full_compliance"        # 100% conforme
    SUBSTANTIAL_COMPLIANCE = "substantial"     # Majoritairement conforme (80-99%)
    PARTIAL_COMPLIANCE = "partial"             # Partiellement conforme (50-79%)
    MINIMAL_COMPLIANCE = "minimal"             # Conformité minimale (25-49%)
    NON_COMPLIANT = "non_compliant"           # Non conforme (0-24%)
    NOT_ASSESSED = "not_assessed"             # Pas encore évalué
    IN_ASSESSMENT = "in_assessment"           # Évaluation en cours