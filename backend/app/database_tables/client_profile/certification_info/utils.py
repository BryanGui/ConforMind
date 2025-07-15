"""
UTILS - Fonctions utilitaires pour certification_info

Gestion du fichier JSON et fonctions métier pour les certifications.
"""

import json
#or_ = Fonction SQLAlchemy pour créer des conditions OU dans les requêtes SQL.
from sqlalchemy import or_
from typing import List, Dict, Any, Optional
from pathlib import Path
from sqlalchemy.orm import Session

# Import des tables (à adapter selon votre structure)
from .certification_info import CertificationMaster

# Chemin vers le fichier JSON
JSON_FILE_PATH = Path(__file__).parent / "certification_list.json"

# ==================== CHARGEMENT JSON ====================

def load_standard_certifications() -> Dict[str, Any]:
    """
    Charge le fichier JSON des certifications standard
    
    Returns:
        Dictionnaire avec métadonnées + liste certifications
        
    Raises:
        FileNotFoundError: Si fichier JSON introuvable
        json.JSONDecodeError: Si JSON malformé
    """
    try:
        with open(JSON_FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Fichier certification_list.json introuvable : {JSON_FILE_PATH}")
    except json.JSONDecodeError:
        raise

def get_certifications_list() -> List[Dict[str, Any]]:
    """
    Retourne uniquement la liste des certifications (sans métadonnées)
    
    Returns:
        Liste des certifications
    """
    data = load_standard_certifications()
    return data.get("certifications", [])

# ==================== POPULATION DATABASE ====================

def populate_certifications_master(db: Session) -> int:
    """
    Peuple la table certifications_master depuis le fichier JSON
    
    Args:
        db: Session SQLAlchemy
        
    Returns:
        Nombre de certifications ajoutées
        
    Raises:
        Exception: Si erreur pendant l'insertion
    """
    try:
        certifications = get_certifications_list()
        added_count = 0
        
        for cert_data in certifications:
            # Vérifier si certification existe déjà
            existing = db.query(CertificationMaster).filter_by(code=cert_data["code"]).first()
            
            if not existing:
                # Créer nouvelle certification
                new_cert = CertificationMaster(
                    code=cert_data["code"],
                    name=cert_data["name"],
                    short_description=cert_data["short_description"],
                    long_description=cert_data.get("long_description", ""),
                    category=cert_data["category"],
                    sector=cert_data.get("sector", "general"),
                    popularity_rank=cert_data.get("popularity_rank", 999),
                    is_active=cert_data.get("is_active", True)
                )
                
                db.add(new_cert)
                added_count += 1
        
        db.commit()
        return added_count
        
    except Exception as e:
        db.rollback()
        raise Exception(f"Erreur lors du populate : {e}")

def check_populate_needed(db: Session) -> bool:
    """
    Vérifie si la table master doit être peuplée
    
    Args:
        db: Session SQLAlchemy
        
    Returns:
        True si populate nécessaire, False sinon
    """
    count = db.query(CertificationMaster).count()
    return count == 0

# ==================== AUTOCOMPLETE & RECHERCHE ====================

def get_certification_suggestions(db: Session, query: str, limit: int = 10) -> List[Dict[str, Any]]:
    """
    Retourne suggestions autocomplete depuis la base + JSON
    
    Args:
        db: Session SQLAlchemy
        query: Texte recherché par l'utilisateur
        limit: Nombre max de suggestions
        
    Returns:
        Liste de suggestions formatées pour autocomplete
    """
    suggestions = []
    
    # Recherche dans la base de données
    db_results = db.query(CertificationMaster).filter(
        CertificationMaster.is_active
    ).filter(
        # Recherche dans code, name ou short_description
        or_(
            CertificationMaster.code.ilike(f"%{query}%"),
            CertificationMaster.name.ilike(f"%{query}%"),
            CertificationMaster.short_description.ilike(f"%{query}%")
        )
    ).order_by(CertificationMaster.popularity_rank).limit(limit).all()
    
    # Formatter pour autocomplete
    for cert in db_results:
        suggestions.append({
            "value": cert.name,
            "label": f"{cert.name} - {cert.short_description}",
            "code": cert.code,
            "description": cert.short_description,
            "long_description": cert.long_description,
            "master_id": cert.id
        })
    
    return suggestions

# ==================== VALIDATION ====================

def validate_certification_exists(db: Session, certification_name: str) -> Optional[CertificationMaster]:
    """
    Valide qu'une certification existe dans la base master
    
    Args:
        db: Session SQLAlchemy
        certification_name: Nom de la certification à valider
        
    Returns:
        CertificationMaster si trouvé, None sinon
    """
    return db.query(CertificationMaster).filter(
        or_(
            CertificationMaster.name == certification_name,
            CertificationMaster.code == certification_name.lower().replace(" ", "_")
        )
    ).first()

# ==================== MÉTADONNÉES JSON ====================

def get_json_metadata() -> Dict[str, Any]:
    """
    Retourne les métadonnées du fichier JSON
    
    Returns:
        Dictionnaire avec version, date, etc.
    """
    data = load_standard_certifications()
    return {
        "version": data.get("version", "unknown"),
        "last_updated": data.get("last_updated", "unknown"),
        "total_certifications": data.get("total_certifications", 0),
        "file_path": str(JSON_FILE_PATH)
    }