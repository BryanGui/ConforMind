"""
DATABASE CONFIGURATION - Engine SQLite + Session Management

Configuration centralisée pour ConforMind-AI :
- Engine SQLite avec support JSON
- Session factory pour FastAPI
- Fonctions d'initialisation
- Dependency injection pour les endpoints
"""

from sqlalchemy import create_engine, event, inspect, text
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.engine import Engine
from typing import Any, Generator, Union, TypedDict, Literal
import sqlite3
import os

# Import de notre architecture database
from app.database_tables import Base
from app.utilities.file_utils import initialize_storage_structure

# Configuration de la base de données
DATABASE_URL = "sqlite:///./conformind_ai.db"

# Création de l'engine avec optimisations SQLite
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False,  # Nécessaire pour SQLite + FastAPI
        "timeout": 20                # Timeout connexion 20s
    },
    echo=False,  # True pour debug SQL
    pool_pre_ping=True  # Vérification connexion
)

# Session factory pour FastAPI
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False, 
    bind=engine
)

# ==================== TYPES ROBUSTES ====================

class HealthyDatabase(TypedDict):
    """Database en bon état"""
    status: Literal["healthy"]
    database_file: str
    connection: str
    file_exists: bool

class UnhealthyDatabase(TypedDict):
    """Database en erreur"""
    status: Literal["unhealthy"]
    database_file: str
    error: str
    file_exists: bool

# Union type pour toutes les réponses possibles
DatabaseHealth = Union[HealthyDatabase, UnhealthyDatabase]

# ==================== ÉVÉNEMENTS SQLITE ====================

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection: Union[sqlite3.Connection, Any], connection_record: Any) -> None:
    """Configure SQLite pour optimiser les performances et activer JSON"""
    try:
        cursor = dbapi_connection.cursor()
        
        # Optimisations SQLite
        cursor.execute("PRAGMA foreign_keys=ON")      # Clés étrangères
        cursor.execute("PRAGMA journal_mode=WAL")     # Write-Ahead Logging (performance)
        cursor.execute("PRAGMA synchronous=NORMAL")   # Balance performance/sécurité
        cursor.execute("PRAGMA cache_size=10000")     # Cache 10MB
        cursor.execute("PRAGMA temp_store=MEMORY")    # Tables temp en mémoire
        
        # Activer les extensions JSON (si disponible)
        try:
            cursor.execute("SELECT json('{}')") 
            print("✅ Support JSON SQLite activé")
        except Exception:
            print("⚠️  JSON SQLite non disponible (version ancienne)")
            
        cursor.close()
    except AttributeError:
        # Pas une connexion SQLite, ignorer
        pass

# ==================== FONCTIONS PRINCIPALES ====================

def create_tables() -> None:
    """Crée toutes les tables dans la base de données"""
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Tables créées avec succès")
        
        # Afficher les tables créées
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        print(f"📋 Tables dans la DB: {', '.join(tables)}")
        
    except Exception as e:
        print(f"❌ Erreur création tables: {e}")
        raise e

def check_database_health() -> DatabaseHealth:
    """Vérifie l'état de la base de données"""
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1")).fetchone()
        db.close()
        
        # Retour typé HealthyDatabase
        return {
            "status": "healthy",
            "database_file": DATABASE_URL,
            "connection": "OK",
            "file_exists": os.path.exists("./conformind_ai.db")
        }
    except Exception as e:
        # Retour typé UnhealthyDatabase
        return {
            "status": "unhealthy", 
            "database_file": DATABASE_URL,
            "error": str(e),
            "file_exists": os.path.exists("./conformind_ai.db")
        }

def initialize_database() -> DatabaseHealth:
    """
    Initialise complètement la base de données et le stockage
    
    Returns:
        DatabaseHealth: État de la base après initialisation
    """
    print("🚀 Initialisation base de données ConforMind-AI...")
    
    try:
        # 1. Créer les tables
        create_tables()
        
        # 2. Créer la structure de stockage fichiers
        initialize_storage_structure() 
        print("✅ Structure de stockage SaaS initialisée")
        
        # 3. Vérifier la santé finale
        health = check_database_health()
        
        # 4. Affichage selon le résultat (type narrowing)
        if health["status"] == "healthy":
            print("✅ Base de données initialisée avec succès")
        else:
            print(f"❌ Erreur initialisation: {health['error']}")
        
        return health
        
    except Exception as e:
        # En cas d'erreur pendant l'initialisation
        print(f"❌ Erreur critique initialisation: {e}")
        return {
            "status": "unhealthy",
            "database_file": DATABASE_URL,
            "error": f"Initialization failed: {str(e)}",
            "file_exists": os.path.exists("./conformind_ai.db")
        }

def reset_database() -> None:
    """
    ATTENTION: Supprime et recrée toutes les tables
    À utiliser UNIQUEMENT en développement
    """
    print("⚠️  RESET DATABASE - Suppression de toutes les données...")
    
    try:
        # Supprimer toutes les tables
        Base.metadata.drop_all(bind=engine)
        print("🗑️  Tables supprimées")
        
        # Recréer les tables
        create_tables()
        
        # Recréer la structure de stockage
        initialize_storage_structure()
        print("✅ Structure de stockage recréée")
        
        print("✅ Database reset terminé")
        
    except Exception as e:
        print(f"❌ Erreur reset database: {e}")
        raise e

# ==================== DEPENDENCY INJECTION ====================

def get_db() -> Generator[Session, None, None]:
    """
    Dependency pour obtenir une session de base de données
    À utiliser dans les endpoints FastAPI
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_test_db() -> Session:
    """Database session pour les tests unitaires"""
    return SessionLocal()