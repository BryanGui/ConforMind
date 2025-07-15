# routers/ai_models.py
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from datetime import datetime, timezone
import uuid
import os
from typing import List, Any
#sql_db import
from sqlalchemy.orm import Session
from app.database_tables import AIModel
from app.core.database import get_db
from app.utilities.file_utils import create_model_storage_directories, get_model_file_path
from app.utilities.auth_temp import get_current_client_id, get_current_user_info

# Import relatif depuis le dossier parent
from app.api_schemas.ai_models import AIModelUploadResponse, AIModelListResponse, AIModelItem, AIModelDeleteResponse


router = APIRouter(prefix="/api/ai-models", tags=["AI Models"])

@router.post("/upload", response_model=AIModelUploadResponse)
async def upload_ai_model(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """
    Upload un modèle IA pour analyse de conformité EU AI Act.
    
    Accepte les formats : .pkl, .joblib, .h5, .onnx, .pt
    Retourne un model_id unique pour référencer le modèle dans les prochains appels API.
    Le fichier est stocké de manière sécurisée et prêt pour l'analyse de conformité.
    """
    
    if not file.filename:
        raise HTTPException(status_code=400, detail="Nom de fichier manquant")
    
    if not file.filename.endswith(('.pkl', '.joblib', '.h5', '.onnx', '.pt')):
        raise HTTPException(
            status_code=400, 
            detail="Format non supporté. Utilisez .pkl, .joblib, .h5, .onnx ou .pt"
        )
    
    # ================================================================
    # TODO MVP: Auth temporaire - client_id hardcodé
    # TODO PHASE 2: Récupérer client_id depuis JWT token
    # ================================================================
    client_id = get_current_client_id()
    user_info = get_current_user_info()
    # ================================================================
    
    model_id = str(uuid.uuid4())
    
    try:
        # ================================================================
        # TODO PHASE 2: Remplacer stockage local par service cloud
        # ================================================================
        content = await file.read()
        file_size_mb = len(content) / (1024 * 1024)
        
        # Créer la structure de stockage SaaS (par client)
        create_model_storage_directories(client_id, model_id)
        upload_path = get_model_file_path(client_id, model_id, file.filename)
        
        with open(upload_path, "wb") as f:
            f.write(content)
        # ================================================================
        
        # Sauvegarder en base de données avec infos client
        ai_model = AIModel(
            id=model_id,
            name=f"Model_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}",
            version="v1.0", 
            creator=user_info["user_email"],  # Email depuis auth temporaire
            file_size_mb=file_size_mb,
            model_file_path=upload_path,
            # TODO: Ajouter client_id en tant que champ dans AIModel
        )
        
        db.add(ai_model)
        db.commit()
        db.refresh(ai_model)
        
        return AIModelUploadResponse(
            model_id=model_id,
            filename=file.filename,
            file_size_bytes=len(content),
            upload_timestamp=datetime.now()
        )
        
    except Exception as e:
        # Nettoyage en cas d'erreur
        if 'model_id' in locals() and 'client_id' in locals():
            try:
                from app.utilities.file_utils import cleanup_model_files
                cleanup_model_files(client_id, model_id)
            except Exception:
                pass  # Ignorer erreurs de nettoyage
        
        raise HTTPException(
            status_code=500, 
            detail=f"Erreur lors de l'upload: {str(e)}"
        )

@router.get("/", response_model=AIModelListResponse)

async def list_ai_models():
    """
    Récupère la liste complète des modèles IA uploadés par le client.
    
    Affiche pour chaque modèle : nom, taille, date d'upload et statut d'analyse.
    Utilisé principalement pour l'interface "Models" où le client gère ses modèles.
    Inclut le nombre total de modèles pour les statistiques client.
    """
    
    # ================================================================
    # TODO PHASE 2: Récupérer depuis base de données avec pagination
    # ================================================================
    import glob
    files = glob.glob("data/client_uploads/*")
    
    models: List[Any] = []
    for file_path in files:
        # Parse filename: {model_id}_{original_filename}
        basename = os.path.basename(file_path)
        model_id = basename.split('_')[0]
        filename = '_'.join(basename.split('_')[1:])
        
        models.append(AIModelItem(
            model_id=model_id,
            filename=filename,
            file_size_bytes=os.path.getsize(file_path),
            upload_timestamp=datetime.fromtimestamp(os.path.getctime(file_path)),
            analysis_status="pending"
        ))
    # ================================================================
    
    return AIModelListResponse(
        models=models,
        total_count=len(models)
    )



# routers/ai_models.py (ajouter après la route GET)

@router.delete("/{model_id}", response_model=AIModelDeleteResponse)
async def delete_ai_model(model_id: str):
    """
    Supprime définitivement un modèle IA et tous ses fichiers associés.
    
    Supprime le fichier modèle, les analyses et rapports générés.
    Action irréversible - utilisé quand le client ne veut plus du modèle.
    Retourne confirmation de suppression avec détails du modèle supprimé.
    """
    
    # ================================================================
    # TODO PHASE 2: Supprimer depuis base de données + storage cloud
    # ================================================================
    import glob
    pattern = f"data/client_uploads/{model_id}_*"
    files = glob.glob(pattern)
    
    if not files:
        raise HTTPException(
            status_code=404, 
            detail=f"Model {model_id} not found"
        )
    
    file_path = files[0]
    filename = file_path.split('_', 1)[1]  # Récupère filename original
    
    # Suppression fichier
    os.remove(file_path)
    

    # ================================================================
    # TODO: Supprimer aussi les rapports et analyses associés
    # ================================================================
    
    return AIModelDeleteResponse(
        model_id=model_id,
        filename=filename,
        deleted=True,
        message=f"Model {filename} deleted successfully"
    )