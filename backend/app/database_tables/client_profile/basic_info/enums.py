"""
ENUMS pour basic_info.py
"""
from enum import Enum

class CompanySize(str, Enum):
    """Taille entreprise selon EU AI Act Article 55"""
    MICRO = "micro"          # 1-9 employés + < 2M€ CA
    SMALL = "small"          # 10-49 employés + < 10M€ CA  
    MEDIUM = "medium"        # 50-249 employés + < 50M€ CA
    LARGE = "large"          # 250+ employés ou > 50M€ CA

class AnnualRevenueEur(str, Enum):
    """Chiffre d'affaires annuel en euros"""
    MICRO = "< 2M€"          # Micro-entreprise
    SMALL = "2-10M€"         # Petite entreprise
    MEDIUM = "10-50M€"       # Moyenne entreprise
    LARGE = "> 50M€"         # Grande entreprise
    PREFER_NOT_SAY = "Non communiqué"

class GeographicalScope(str, Enum):
    """Périmètre géographique d'activité"""
    EU_ONLY = "eu_only"                    # Europe uniquement
    EU_INTERNATIONAL = "eu_international"  # Europe + International
    INTERNATIONAL_EU_USERS = "intl_eu_users"  # International avec utilisateurs EU