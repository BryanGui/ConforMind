"""
ENUMS CERTIFICATION - EU AI Act Focus ConforMind-AI

Certifications liées directement à l'EU AI Act et à son écosystème.
Focus uniquement sur les standards qui ont un impact sur la conformité IA.

Catégories :
- EU AI Act (cœur ConforMind)
- Standards ISO liés IA (nouveaux standards spécifiques)
- Compliance données (GDPR, impact direct sur IA)
- Sectoriel high-risk (finance, santé = domaines high-risk EU AI Act)
"""

import enum

# ==================== EU AI ACT - CŒUR CONFORMIND ====================

class EUAIActCompliance(enum.Enum):
    """EU AI Act - Conformité directe (Articles 42-43)"""
    
    # Conformité générale EU AI Act
    EU_AI_ACT_COMPLIANT = "EU_AI_ACT_COMPLIANT"                    # Article 16 - Conformité générale
    EU_AI_ACT_HIGH_RISK_CERTIFIED = "EU_AI_ACT_HIGH_RISK_CERTIFIED"  # Article 43 - Systèmes haut risque
    EU_AI_ACT_CONFORMITY_ASSESSMENT = "EU_AI_ACT_CONFORMITY_ASSESSMENT"  # Article 43 - Évaluation conformité
    
    # Marquage CE pour IA (Article 49)
    EU_AI_ACT_CE_MARKING = "EU_AI_ACT_CE_MARKING"                  # Marquage CE obligatoire high-risk

# ==================== STANDARDS ISO SPÉCIFIQUES IA ====================

class ISOAIStandard(enum.Enum):
    """Standards ISO développés spécifiquement pour l'IA (requis EU AI Act)"""
    
    # Standards IA (mentionnés dans EU AI Act Article 40)
    ISO_23053 = "ISO_23053"        # Framework pour l'IA et big data
    ISO_23894 = "ISO_23894"        # Gestion des risques IA (AI risk management)
    ISO_24027 = "ISO_24027"        # Biais en intelligence artificielle
    
    # Sécurité données + IA
    ISO_27001 = "ISO_27001"        # Sécurité information (base pour systèmes IA)
    ISO_27701 = "ISO_27701"        # Privacy (complément GDPR pour IA)

# ==================== COMPLIANCE DONNÉES (Impact IA) ====================

class DataPrivacyCompliance(enum.Enum):
    """Protection données - impact direct sur systèmes IA (Article 10 EU AI Act)"""
    
    # EU - Protection données
    GDPR_COMPLIANT = "GDPR_COMPLIANT"             # GDPR (Article 10 EU AI Act - données training)
    GDPR_DPO_CERTIFIED = "GDPR_DPO_CERTIFIED"     # DPO certifié (gouvernance données IA)
    
    # US - Protection données (multinationales IA)
    CCPA = "CCPA"                                 # California Consumer Privacy Act

# ==================== SECTORIEL HIGH-RISK EU AI ACT ====================

class FinancialAICompliance(enum.Enum):
    """Finance - Annexe III EU AI Act (high-risk domain)"""
    
    # Standards finance requis pour IA high-risk
    SOX = "SOX"                                   # Sarbanes-Oxley (audit trail IA)
    MIFID_II = "MIFID_II"                        # Transparence algorithmes finance EU
    PCI_DSS = "PCI_DSS"                          # Sécurité paiements (IA fraud detection)

class HealthcareAICompliance(enum.Enum):
    """Santé - Annexe III EU AI Act (high-risk domain)"""
    
    # Standards santé requis pour IA high-risk  
    ISO_13485 = "ISO_13485"                      # Dispositifs médicaux (IA médicale)
    HIPAA = "HIPAA"                              # Protection données santé US
    HDS_CERTIFICATION = "HDS_CERTIFICATION"      # Hébergement données santé France

class EducationAICompliance(enum.Enum):
    """Éducation - Annexe III EU AI Act (high-risk domain)"""
    
    # Standards éducation pour IA high-risk
    FERPA = "FERPA"                              # Protection données étudiants US
    WCAG_AA = "WCAG_AA"                          # Accessibilité (IA éducative)

# ==================== ENUM UNIFIÉE POUR API CONFORMIND ====================

class CertificationType(enum.Enum):
    """
    Enum principale pour ConforMind-AI
    UNIQUEMENT les certifications avec impact direct EU AI Act
    """
    
    # ===== CŒUR EU AI ACT =====
    EU_AI_ACT_COMPLIANT = "EU_AI_ACT_COMPLIANT"
    EU_AI_ACT_HIGH_RISK_CERTIFIED = "EU_AI_ACT_HIGH_RISK_CERTIFIED"
    EU_AI_ACT_CONFORMITY_ASSESSMENT = "EU_AI_ACT_CONFORMITY_ASSESSMENT"
    EU_AI_ACT_CE_MARKING = "EU_AI_ACT_CE_MARKING"
    
    # ===== STANDARDS ISO IA =====
    ISO_23053 = "ISO_23053"        # Framework IA et big data
    ISO_23894 = "ISO_23894"        # Gestion risques IA
    ISO_24027 = "ISO_24027"        # Biais IA
    ISO_27001 = "ISO_27001"        # Sécurité information (base IA)
    ISO_27701 = "ISO_27701"        # Privacy + IA
    
    # ===== COMPLIANCE DONNÉES (Impact IA) =====
    GDPR_COMPLIANT = "GDPR_COMPLIANT"
    GDPR_DPO_CERTIFIED = "GDPR_DPO_CERTIFIED"
    CCPA = "CCPA"
    
    # ===== HIGH-RISK DOMAINS =====
    # Finance (Annexe III)
    SOX = "SOX"
    MIFID_II = "MIFID_II"
    PCI_DSS = "PCI_DSS"
    
    # Santé (Annexe III)
    ISO_13485 = "ISO_13485"
    HIPAA = "HIPAA"
    HDS_CERTIFICATION = "HDS_CERTIFICATION"
    
    # Éducation (Annexe III)
    FERPA = "FERPA"
    WCAG_AA = "WCAG_AA"

# ==================== MÉTADONNÉES EU AI ACT ====================

class CertificationMetadata:
    """Métadonnées centrées EU AI Act"""
    
    EU_AI_ACT_INFO = {
        # EU AI Act core
        CertificationType.EU_AI_ACT_COMPLIANT: {
            "name": "EU AI Act Compliance",
            "description": "Conformité générale au Règlement européen sur l'IA",
            "eu_ai_act_article": "Article 16",
            "mandatory_for": ["Tous systèmes IA déployés en EU"],
            "validity_period": "Monitoring continu",
            "priority": "CRITIQUE"
        },
        
        CertificationType.EU_AI_ACT_HIGH_RISK_CERTIFIED: {
            "name": "EU AI Act High-Risk Certification", 
            "description": "Certification pour systèmes IA haut risque",
            "eu_ai_act_article": "Article 43",
            "mandatory_for": ["Systèmes Annexe III (finance, santé, RH, etc.)"],
            "validity_period": "Évaluation continue",
            "priority": "CRITIQUE"
        },
        
        # Standards ISO IA
        CertificationType.ISO_23894: {
            "name": "ISO 23894 - AI Risk Management",
            "description": "Standard gestion des risques IA",
            "eu_ai_act_article": "Article 40 (standards harmonisés)",
            "mandatory_for": ["Recommandé systèmes high-risk"],
            "validity_period": "3 ans", 
            "priority": "HAUTE"
        },
        
        # Compliance données
        CertificationType.GDPR_COMPLIANT: {
            "name": "GDPR Compliance",
            "description": "Protection données personnelles",
            "eu_ai_act_article": "Article 10 (données training)",
            "mandatory_for": ["Systèmes IA traitant données personnelles"],
            "validity_period": "Continu",
            "priority": "CRITIQUE"
        }
    }
    
    @classmethod
    def get_eu_ai_act_related_certs(cls) -> list:
        """Certifications directement liées EU AI Act"""
        return [
            CertificationType.EU_AI_ACT_COMPLIANT,
            CertificationType.EU_AI_ACT_HIGH_RISK_CERTIFIED,
            CertificationType.ISO_23894,
            CertificationType.ISO_24027,
            CertificationType.GDPR_COMPLIANT
        ]
    
    @classmethod
    def get_high_risk_domain_certs(cls, domain: str) -> list:
        """Certifications par domaine high-risk Annexe III"""
        domain_mapping = {
            "finance": [CertificationType.SOX, CertificationType.MIFID_II, CertificationType.PCI_DSS],
            "healthcare": [CertificationType.ISO_13485, CertificationType.HIPAA, CertificationType.HDS_CERTIFICATION],
            "education": [CertificationType.FERPA, CertificationType.WCAG_AA]
        }
        return domain_mapping.get(domain.lower(), [])

# ==================== EXPORTS ====================

__all__ = [
    "CertificationType",
    "EUAIActCompliance", 
    "ISOAIStandard",
    "DataPrivacyCompliance",
    "FinancialAICompliance",
    "HealthcareAICompliance",
    "EducationAICompliance",
    "CertificationMetadata"
]