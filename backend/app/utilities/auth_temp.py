"""
AUTH TEMPORAIRE - MVP ConforMind-AI

Système d'authentification temporaire pour le MVP.
À remplacer par un système robuste en production.

TODO PHASE 2:
- Implémenter JWT tokens
- Système multi-organisations
- Gestion des rôles utilisateurs
- Auth sécurisée avec hashage passwords
- Session management
- Rate limiting
"""

from typing import Dict, Any

# ================================================================
# TODO MVP: Client/Organisation hardcodés pour tests
# TODO PHASE 2: Récupérer depuis base de données auth
# ================================================================
MVP_TEST_CLIENT = {
    "client_id": "mvp_test_client_001",
    "organization_name": "ConforMind Test Organization",
    "user_id": "test_user_001",
    "user_email": "test@conformind.ai",
    "subscription_tier": "enterprise"  # Pour tests complets
}

def get_current_client_id() -> str:
    """
    TODO MVP: Retourne client_id hardcodé pour tests
    TODO PHASE 2: Extraire client_id depuis JWT token
    
    Returns:
        ID du client/organisation actuel
    """
    return MVP_TEST_CLIENT["client_id"]

def get_current_user_info() -> Dict[str, Any]:
    """
    TODO MVP: Retourne infos utilisateur hardcodées
    TODO PHASE 2: Récupérer depuis token JWT décodé
    
    Returns:
        Dictionnaire avec infos utilisateur/organisation
    """
    return MVP_TEST_CLIENT.copy()

def get_current_organization_name() -> str:
    """
    TODO MVP: Retourne nom organisation hardcodé
    TODO PHASE 2: Récupérer depuis base données
    
    Returns:
        Nom de l'organisation
    """
    return MVP_TEST_CLIENT["organization_name"]

# ================================================================
# TODO PHASE 2: Fonctions à implémenter pour production
# ================================================================

def verify_jwt_token(token: str) -> Dict[str, Any]:
    """
    TODO PHASE 2: Vérifier et décoder JWT token
    
    Args:
        token: JWT token depuis header Authorization
        
    Returns:
        Payload décodé avec user_id, client_id, etc.
        
    Raises:
        HTTPException: Si token invalide/expiré
    """
    raise NotImplementedError("À implémenter en PHASE 2")

def create_jwt_token(user_id: str, client_id: str) -> str:
    """
    TODO PHASE 2: Créer JWT token pour utilisateur
    
    Args:
        user_id: ID utilisateur
        client_id: ID organisation
        
    Returns:
        JWT token signé
    """
    raise NotImplementedError("À implémenter en PHASE 2")

def authenticate_user(email: str, password: str) -> Dict[str, Any]:
    """
    TODO PHASE 2: Authentifier utilisateur
    
    Args:
        email: Email utilisateur
        password: Mot de passe (sera hashé)
        
    Returns:
        Infos utilisateur si auth réussie
        
    Raises:
        HTTPException: Si credentials invalides
    """
    raise NotImplementedError("À implémenter en PHASE 2")

def check_subscription_limits(client_id: str, operation: str) -> bool:
    """
    TODO PHASE 2: Vérifier limites abonnement
    
    Args:
        client_id: ID organisation
        operation: Type d'opération (upload_model, generate_report, etc.)
        
    Returns:
        True si opération autorisée, False sinon
    """
    # Pour MVP: tout autorisé
    return True