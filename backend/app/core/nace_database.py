"""
NACE CODES DATABASE - Classification complète EU

Base de données complète des codes NACE (Nomenclature des Activités économiques 
dans la Communauté Européenne) avec mapping vers domaines de risque EU AI Act.

Niveaux:
- Niveau 1: Sections (A, B, C, etc.)
- Niveau 2: Divisions (01, 02, 03, etc.)
- Niveau 3: Groupes (01.1, 01.2, etc.)
- Niveau 4: Classes (01.11, 01.12, etc.)

Pour ConforMind: Focus sur niveaux 1 et 2 pour le questionnaire, 
puis possibilité de préciser niveau 3-4.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum
import json

# Import des enums depuis notre code existant
from .company import RiskDomain

@dataclass
class NaceCode:
    """Structure d'un code NACE avec métadonnées"""
    code: str                           # "A", "01", "01.1", "01.11"
    level: int                          # 1, 2, 3, 4
    description: str                    # Description française
    description_en: str                 # Description anglaise
    parent_code: Optional[str] = None   # Code parent (ex: "01.1" → parent "01")
    risk_domains: List[RiskDomain] = None
    
    def __post_init__(self):
        if self.risk_domains is None:
            self.risk_domains = []

# ==================== NACE DATABASE COMPLÈTE ====================

class NaceDatabase:
    """Base de données complète des codes NACE"""
    
    def __init__(self):
        self.codes = self._initialize_nace_codes()
    
    def _initialize_nace_codes(self) -> Dict[str, NaceCode]:
        """Initialise la base complète des codes NACE"""
        codes = {}
        
        # ===================== NIVEAU 1 - SECTIONS =====================
        
        # Section A - Agriculture, sylviculture et pêche
        codes["A"] = NaceCode(
            code="A", level=1,
            description="Agriculture, sylviculture et pêche",
            description_en="Agriculture, forestry and fishing",
            risk_domains=[]  # Généralement minimal risk
        )
        
        # Section B - Industries extractives
        codes["B"] = NaceCode(
            code="B", level=1,
            description="Industries extractives",
            description_en="Mining and quarrying",
            risk_domains=[RiskDomain.CRITICAL_INFRASTRUCTURE]
        )
        
        # Section C - Industrie manufacturière
        codes["C"] = NaceCode(
            code="C", level=1,
            description="Industrie manufacturière",
            description_en="Manufacturing",
            risk_domains=[RiskDomain.CRITICAL_INFRASTRUCTURE]
        )
        
        # Section D - Production et distribution d'électricité, de gaz, de vapeur et d'air conditionné
        codes["D"] = NaceCode(
            code="D", level=1,
            description="Production et distribution d'électricité, de gaz, de vapeur et d'air conditionné",
            description_en="Electricity, gas, steam and air conditioning supply",
            risk_domains=[RiskDomain.CRITICAL_INFRASTRUCTURE]
        )
        
        # Section E - Production et distribution d'eau
        codes["E"] = NaceCode(
            code="E", level=1,
            description="Production et distribution d'eau; assainissement, gestion des déchets et dépollution",
            description_en="Water supply; sewerage, waste management and remediation activities",
            risk_domains=[RiskDomain.CRITICAL_INFRASTRUCTURE]
        )
        
        # Section F - Construction
        codes["F"] = NaceCode(
            code="F", level=1,
            description="Construction",
            description_en="Construction",
            risk_domains=[]
        )
        
        # Section G - Commerce de gros et de détail
        codes["G"] = NaceCode(
            code="G", level=1,
            description="Commerce; réparation d'automobiles et de motocycles",
            description_en="Wholesale and retail trade; repair of motor vehicles and motorcycles",
            risk_domains=[]
        )
        
        # Section H - Transports et entreposage
        codes["H"] = NaceCode(
            code="H", level=1,
            description="Transports et entreposage",
            description_en="Transportation and storage",
            risk_domains=[RiskDomain.CRITICAL_INFRASTRUCTURE]
        )
        
        # Section I - Hébergement et restauration
        codes["I"] = NaceCode(
            code="I", level=1,
            description="Hébergement et restauration",
            description_en="Accommodation and food service activities",
            risk_domains=[]
        )
        
        # Section J - Information et communication
        codes["J"] = NaceCode(
            code="J", level=1,
            description="Information et communication",
            description_en="Information and communication",
            risk_domains=[RiskDomain.CRITICAL_INFRASTRUCTURE]
        )
        
        # Section K - Activités financières et d'assurance ⭐ HIGH RISK
        codes["K"] = NaceCode(
            code="K", level=1,
            description="Activités financières et d'assurance",
            description_en="Financial and insurance activities",
            risk_domains=[RiskDomain.ESSENTIAL_SERVICES, RiskDomain.EMPLOYMENT]
        )
        
        # Section L - Activités immobilières
        codes["L"] = NaceCode(
            code="L", level=1,
            description="Activités immobilières",
            description_en="Real estate activities",
            risk_domains=[]
        )
        
        # Section M - Activités spécialisées, scientifiques et techniques
        codes["M"] = NaceCode(
            code="M", level=1,
            description="Activités spécialisées, scientifiques et techniques",
            description_en="Professional, scientific and technical activities",
            risk_domains=[RiskDomain.EMPLOYMENT]  # Conseil RH
        )
        
        # Section N - Activités de services administratifs et de soutien ⭐ HIGH RISK RH
        codes["N"] = NaceCode(
            code="N", level=1,
            description="Activités de services administratifs et de soutien",
            description_en="Administrative and support service activities",
            risk_domains=[RiskDomain.EMPLOYMENT]  # Agences intérim, recrutement
        )
        
        # Section O - Administration publique
        codes["O"] = NaceCode(
            code="O", level=1,
            description="Administration publique",
            description_en="Public administration and defence; compulsory social security",
            risk_domains=[RiskDomain.ESSENTIAL_SERVICES, RiskDomain.LAW_ENFORCEMENT, RiskDomain.JUSTICE_DEMOCRACY]
        )
        
        # Section P - Enseignement ⭐ HIGH RISK
        codes["P"] = NaceCode(
            code="P", level=1,
            description="Enseignement",
            description_en="Education",
            risk_domains=[RiskDomain.EDUCATION]
        )
        
        # Section Q - Santé humaine et action sociale ⭐ HIGH RISK
        codes["Q"] = NaceCode(
            code="Q", level=1,
            description="Santé humaine et action sociale",
            description_en="Human health and social work activities",
            risk_domains=[RiskDomain.ESSENTIAL_SERVICES]
        )
        
        # Section R - Arts, spectacles et activités récréatives
        codes["R"] = NaceCode(
            code="R", level=1,
            description="Arts, spectacles et activités récréatives",
            description_en="Arts, entertainment and recreation",
            risk_domains=[]
        )
        
        # Section S - Autres activités de services
        codes["S"] = NaceCode(
            code="S", level=1,
            description="Autres activités de services",
            description_en="Other service activities",
            risk_domains=[]
        )
        
        # Section T - Activités des ménages
        codes["T"] = NaceCode(
            code="T", level=1,
            description="Activités des ménages en tant qu'employeurs",
            description_en="Activities of households as employers",
            risk_domains=[]
        )
        
        # Section U - Activités des organisations extraterritoriales
        codes["U"] = NaceCode(
            code="U", level=1,
            description="Activités des organisations et organismes extraterritoriaux",
            description_en="Activities of extraterritorial organisations and bodies",
            risk_domains=[]
        )
        
        # ===================== NIVEAU 2 - DIVISIONS IMPORTANTES =====================
        
        # Division 64 - Activités des services financiers ⭐ TRÈS HIGH RISK
        codes["64"] = NaceCode(
            code="64", level=2, parent_code="K",
            description="Activités des services financiers, hors assurance et caisses de retraite",
            description_en="Financial service activities, except insurance and pension funding",
            risk_domains=[RiskDomain.ESSENTIAL_SERVICES]
        )
        
        # Division 65 - Assurance ⭐ HIGH RISK
        codes["65"] = NaceCode(
            code="65", level=2, parent_code="K",
            description="Assurance",
            description_en="Insurance, reinsurance and pension funding",
            risk_domains=[RiskDomain.ESSENTIAL_SERVICES]
        )
        
        # Division 66 - Activités auxiliaires de services financiers
        codes["66"] = NaceCode(
            code="66", level=2, parent_code="K",
            description="Activités auxiliaires de services financiers et d'assurance",
            description_en="Activities auxiliary to financial services and insurance activities",
            risk_domains=[RiskDomain.ESSENTIAL_SERVICES]
        )
        
        # Division 78 - Activités liées à l'emploi ⭐ TRÈS HIGH RISK RH
        codes["78"] = NaceCode(
            code="78", level=2, parent_code="N",
            description="Activités liées à l'emploi",
            description_en="Employment activities",
            risk_domains=[RiskDomain.EMPLOYMENT]
        )
        
        # Division 80 - Enquêtes et sécurité ⭐ HIGH RISK BIOMÉTRIE
        codes["80"] = NaceCode(
            code="80", level=2, parent_code="N",
            description="Enquêtes et sécurité",
            description_en="Security and investigation activities",
            risk_domains=[RiskDomain.BIOMETRICS, RiskDomain.LAW_ENFORCEMENT]
        )
        
        # Division 85 - Enseignement ⭐ HIGH RISK
        codes["85"] = NaceCode(
            code="85", level=2, parent_code="P",
            description="Enseignement",
            description_en="Education",
            risk_domains=[RiskDomain.EDUCATION]
        )
        
        # Division 86 - Activités pour la santé humaine ⭐ HIGH RISK
        codes["86"] = NaceCode(
            code="86", level=2, parent_code="Q",
            description="Activités pour la santé humaine",
            description_en="Human health activities",
            risk_domains=[RiskDomain.ESSENTIAL_SERVICES]
        )
        
        # Division 87 - Hébergement médico-social et social
        codes["87"] = NaceCode(
            code="87", level=2, parent_code="Q",
            description="Hébergement médico-social et social",
            description_en="Residential care activities",
            risk_domains=[RiskDomain.ESSENTIAL_SERVICES]
        )
        
        # Division 88 - Action sociale sans hébergement
        codes["88"] = NaceCode(
            code="88", level=2, parent_code="Q",
            description="Action sociale sans hébergement",
            description_en="Social work activities without accommodation",
            risk_domains=[RiskDomain.ESSENTIAL_SERVICES]
        )
        
        # Divisions Infrastructure critique
        codes["35"] = NaceCode(
            code="35", level=2, parent_code="D",
            description="Production et distribution d'électricité, de gaz, de vapeur et d'air conditionné",
            description_en="Electricity, gas, steam and air conditioning supply",
            risk_domains=[RiskDomain.CRITICAL_INFRASTRUCTURE]
        )
        
        codes["36"] = NaceCode(
            code="36", level=2, parent_code="E",
            description="Captage, traitement et distribution d'eau",
            description_en="Water collection, treatment and supply",
            risk_domains=[RiskDomain.CRITICAL_INFRASTRUCTURE]
        )
        
        codes["61"] = NaceCode(
            code="61", level=2, parent_code="J",
            description="Télécommunications",
            description_en="Telecommunications",
            risk_domains=[RiskDomain.CRITICAL_INFRASTRUCTURE]
        )
        
        codes["62"] = NaceCode(
            code="62", level=2, parent_code="J",
            description="Programmation, conseil et autres activités informatiques",
            description_en="Computer programming, consultancy and related activities",
            risk_domains=[]  # Dépend de l'usage
        )
        
        codes["63"] = NaceCode(
            code="63", level=2, parent_code="J",
            description="Services d'information",
            description_en="Information service activities",
            risk_domains=[]
        )
        
        # E-commerce
        codes["47"] = NaceCode(
            code="47", level=2, parent_code="G",
            description="Commerce de détail, à l'exception des automobiles et des motocycles",
            description_en="Retail trade, except of motor vehicles and motorcycles",
            risk_domains=[]
        )
        
        return codes
    
    def get_level_1_codes(self) -> List[NaceCode]:
        """Retourne tous les codes NACE niveau 1 (sections)"""
        return [code for code in self.codes.values() if code.level == 1]
    
    def get_level_2_codes(self, parent_section: Optional[str] = None) -> List[NaceCode]:
        """Retourne tous les codes NACE niveau 2 (divisions)"""
        level_2_codes = [code for code in self.codes.values() if code.level == 2]
        
        if parent_section:
            level_2_codes = [code for code in level_2_codes if code.parent_code == parent_section]
        
        return level_2_codes
    
    def get_high_risk_codes(self) -> List[NaceCode]:
        """Retourne les codes NACE avec domaines de risque HIGH RISK"""
        high_risk_domains = {
            RiskDomain.BIOMETRICS,
            RiskDomain.EDUCATION,
            RiskDomain.EMPLOYMENT,
            RiskDomain.ESSENTIAL_SERVICES,
            RiskDomain.LAW_ENFORCEMENT
        }
        
        return [
            code for code in self.codes.values() 
            if any(domain in high_risk_domains for domain in code.risk_domains)
        ]
    
    def search_by_keyword(self, keyword: str, level: Optional[int] = None) -> List[NaceCode]:
        """Recherche NACE par mot-clé dans la description"""
        keyword_lower = keyword.lower()
        results = []
        
        for code in self.codes.values():
            if level and code.level != level:
                continue
                
            if (keyword_lower in code.description.lower() or 
                keyword_lower in code.description_en.lower()):
                results.append(code)
        
        return results
    
    def get_code_info(self, code: str) -> Optional[NaceCode]:
        """Récupère les infos d'un code NACE spécifique"""
        return self.codes.get(code)
    
    def get_dropdown_data(self) -> Dict[str, List[Dict[str, str]]]:
        """Retourne les données formatées pour dropdown frontend"""
        
        # Niveau 1 pour sélection principale
        level_1_data = []
        for code in self.get_level_1_codes():
            level_1_data.append({
                "value": code.code,
                "label": f"{code.code} - {code.description}",
                "risk_level": "HIGH" if code.risk_domains else "LOW",
                "risk_domains": [domain.value for domain in code.risk_domains]
            })
        
        # Niveau 2 pour spécialisation
        level_2_data = []
        for code in self.get_level_2_codes():
            level_2_data.append({
                "value": code.code,
                "label": f"{code.code} - {code.description}",
                "parent": code.parent_code,
                "risk_level": "HIGH" if code.risk_domains else "LOW", 
                "risk_domains": [domain.value for domain in code.risk_domains]
            })
        
        return {
            "level_1": sorted(level_1_data, key=lambda x: x["value"]),
            "level_2": sorted(level_2_data, key=lambda x: x["value"])
        }

# ==================== FONCTIONS UTILITAIRES ====================

def get_nace_suggestions_for_questionnaire() -> Dict[str, List[Dict[str, str]]]:
    """
    Retourne les suggestions NACE pour le questionnaire Phase 1
    
    Optimisé pour l'UX : codes les plus pertinents d'abord
    """
    db = NaceDatabase()
    
    # Codes NACE les plus pertinents pour l'EU AI Act
    priority_codes = {
        # Finance (très high risk)
        "K": "Activités financières et d'assurance",
        "64": "Services financiers (banques, crédit)",
        "65": "Assurance",
        
        # RH/Emploi (très high risk)
        "N": "Services administratifs et de soutien",
        "78": "Activités liées à l'emploi (recrutement)",
        
        # Santé (high risk)
        "Q": "Santé humaine et action sociale",
        "86": "Activités pour la santé humaine",
        
        # Éducation (high risk)
        "P": "Enseignement",
        "85": "Enseignement",
        
        # Tech/Telecom (infrastructure critique)
        "J": "Information et communication",
        "61": "Télécommunications",
        "62": "Programmation informatique",
        
        # Sécurité (biométrie)
        "80": "Enquêtes et sécurité",
        
        # Commerce/E-commerce
        "G": "Commerce de gros et de détail",
        "47": "Commerce de détail",
        
        # Administration
        "O": "Administration publique"
    }
    
    suggestions = {
        "high_priority": [],
        "standard": []
    }
    
    # Codes haute priorité (secteurs à fort risque EU AI Act)
    for code in ["K", "64", "65", "78", "Q", "86", "P", "85", "80"]:
        nace_info = db.get_code_info(code)
        if nace_info:
            suggestions["high_priority"].append({
                "value": code,
                "label": f"{code} - {nace_info.description}",
                "risk_domains": [domain.value for domain in nace_info.risk_domains]
            })
    
    # Codes standard (autres secteurs)
    for code in ["J", "61", "62", "G", "47", "O", "C", "H"]:
        nace_info = db.get_code_info(code)
        if nace_info:
            suggestions["standard"].append({
                "value": code,
                "label": f"{code} - {nace_info.description}",
                "risk_domains": [domain.value for domain in nace_info.risk_domains]
            })
    
    return suggestions

def export_nace_database_to_json(filepath: str) -> None:
    """Exporte la base NACE en JSON pour le frontend"""
    db = NaceDatabase()
    
    export_data = {
        "metadata": {
            "version": "2024",
            "description": "NACE codes database for EU AI Act compliance",
            "total_codes": len(db.codes)
        },
        "dropdown_data": db.get_dropdown_data(),
        "suggestions": get_nace_suggestions_for_questionnaire(),
        "high_risk_codes": [
            {
                "code": code.code,
                "description": code.description,
                "risk_domains": [domain.value for domain in code.risk_domains]
            }
            for code in db.get_high_risk_codes()
        ]
    }
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(export_data, f, indent=2, ensure_ascii=False)

# ==================== DEMO & TESTS ====================

if __name__ == "__main__":
    # Test de la base NACE
    db = NaceDatabase()
    
    print("🏛️ Base NACE ConforMind - Tests")
    print("=" * 50)
    
    # Test sections niveau 1
    print(f"📊 Sections niveau 1: {len(db.get_level_1_codes())}")
    for code in db.get_level_1_codes()[:5]:
        domains = ", ".join([d.value for d in code.risk_domains]) if code.risk_domains else "Aucun"
        print(f"  {code.code} - {code.description[:50]}... (Risques: {domains})")
    
    print(f"\n📋 Divisions niveau 2: {len(db.get_level_2_codes())}")
    for code in db.get_level_2_codes()[:5]:
        domains = ", ".join([d.value for d in code.risk_domains]) if code.risk_domains else "Aucun"
        print(f"  {code.code} - {code.description[:50]}... (Risques: {domains})")
    
    # Test codes high risk
    print(f"\n🔴 Codes HIGH RISK: {len(db.get_high_risk_codes())}")
    for code in db.get_high_risk_codes():
        print(f"  {code.code} - {code.description[:50]}...")
    
    # Test recherche
    print(f"\n🔍 Recherche 'financ':")
    results = db.search_by_keyword("financ")
    for result in results[:3]:
        print(f"  {result.code} - {result.description}")
    
    # Test suggestions questionnaire
    print(f"\n🎯 Suggestions questionnaire:")
    suggestions = get_nace_suggestions_for_questionnaire()
    print(f"  High priority: {len(suggestions['high_priority'])}")
    print(f"  Standard: {len(suggestions['standard'])}")
    
    # Export JSON
    export_nace_database_to_json("nace_database.json")
    print(f"\n✅ Base NACE exportée vers: nace_database.json")