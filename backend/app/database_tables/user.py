"""
USER MODEL - Table simple pour tests MVP

Table basique pour avoir un utilisateur de test pendant le développement.
À enrichir plus tard selon les besoins.
"""

from sqlalchemy import Column, String, Boolean, DateTime
from datetime import datetime, timezone
import uuid

from .models import Base

class User(Base):
    """
    Table utilisateur simple pour tests MVP
    """
    __tablename__ = "users"
    
    # Identifiant
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    
    # Infos basiques
    username = Column(String, default="test_user")
    email = Column(String, default="test@conformind.ai")
    organization = Column(String, default="Test Organization")
    
    # Statut
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    
    # Pour les tests
    is_test_user = Column(Boolean, default=True)