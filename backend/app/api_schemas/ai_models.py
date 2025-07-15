# api_schemas/ai_model_schema.py
from pydantic import BaseModel
from datetime import datetime

class AIModelUploadResponse(BaseModel):
    model_id: str                    # UUID généré pour ce modèle
    filename: str                    # Nom du fichier uploadé  
    file_size_bytes: int            # Taille du fichier
    upload_timestamp: datetime      # Quand uploadé

class AIModelItem(BaseModel):
    model_id: str
    filename: str
    file_size_bytes: int
    upload_timestamp: datetime
    analysis_status: str              # "pending" | "completed" | "failed"

class AIModelListResponse(BaseModel):
    models: list[AIModelItem]
    total_count: int

class AIModelDeleteResponse(BaseModel):
    model_id: str
    filename: str
    deleted: bool
    message: str