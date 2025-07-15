# routers/reports.py
from fastapi import APIRouter, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
from datetime import datetime
from typing import Optional

# Import des schémas depuis api_schemas/
from app.api_schemas.reports import (
    ReportType,
    ReportRequest,
    ReportGenerationResponse,
    ReportItem,
    ReportListResponse,
    ReportStatusResponse,
    ReportDeleteResponse
)


router = APIRouter(prefix="/reports", tags=["Reports"])

# ==================== ROUTES ====================

@router.post("/generate/{model_id}", response_model=ReportGenerationResponse)
async def generate_report(model_id: int, request: ReportRequest, background_tasks: BackgroundTasks):
    """
    Générer un rapport pour un modèle IA spécifique
    Traitement en arrière-plan avec suivi de progression
    """
    # TODO: Vérifier que le model_id existe
    # TODO: Générer report_id unique
    # TODO: Lancer tâche en arrière-plan selon report_type
    
    report_id = f"rpt_{model_id}_{int(datetime.now().timestamp())}"
    
    if request.report_type == ReportType.COMPLIANCE:
        # TODO: background_tasks.add_task(generate_compliance_report, model_id, request.options, report_id)
        estimated_time = datetime.now().replace(minute=datetime.now().minute + 5)  # 5 min
        message = "Génération rapport de conformité EU AI Act en cours"
        
    elif request.report_type == ReportType.BIAS_ANALYSIS:
        # TODO: background_tasks.add_task(generate_bias_report, model_id, request.options, report_id)
        estimated_time = datetime.now().replace(minute=datetime.now().minute + 3)  # 3 min
        message = "Analyse de biais en cours"
        
    elif request.report_type == ReportType.FULL_AUDIT:
        # TODO: background_tasks.add_task(generate_full_audit, model_id, request.options, report_id)
        estimated_time = datetime.now().replace(minute=datetime.now().minute + 10)  # 10 min
        message = "Audit complet en cours (analyse + conformité + recommandations)"
        
    elif request.report_type == ReportType.RISK_ASSESSMENT:
        # TODO: background_tasks.add_task(generate_risk_assessment, model_id, request.options, report_id)
        estimated_time = datetime.now().replace(minute=datetime.now().minute + 4)  # 4 min
        message = "Évaluation des risques en cours"
        
    else:
        raise HTTPException(status_code=400, detail=f"Type de rapport non supporté: {request.report_type}")
    
    # TODO: Sauvegarder en base le statut initial
    
    return ReportGenerationResponse(
        report_id=report_id,
        status="queued",
        model_id=model_id,
        report_type=request.report_type.value,
        estimated_completion_time=estimated_time,
        message=message
    )

@router.get("/status/{report_id}", response_model=ReportStatusResponse)
async def get_report_status(report_id: str):
    """
    Vérifier le statut de génération d'un rapport
    Utilisé par le frontend pour polling
    """
    # TODO: Récupérer statut depuis base de données
    # TODO: Calculer progress_percent basé sur étapes
    
    # Mock response pour développement
    return ReportStatusResponse(
        report_id=report_id,
        status="completed",  # TODO: Real status from DB
        progress_percent=100,
        current_step="Génération PDF finalisée",
        download_url=f"/api/reports/download/{report_id}"
    )

@router.get("/download/{report_id}")
async def download_report(report_id: str):
    """
    Télécharger le fichier PDF d'un rapport généré
    """
    # TODO: Vérifier que rapport existe et est completed
    # TODO: Vérifier permissions utilisateur
    # TODO: Retourner le vrai fichier PDF
    
    file_path = f"data/generated_reports/{report_id}.pdf"
    
    # TODO: Vérifier que fichier existe
    # if not os.path.exists(file_path):
    #     raise HTTPException(status_code=404, detail="Rapport non trouvé")
    
    return FileResponse(
        path=file_path,
        filename=f"rapport_{report_id}.pdf",
        media_type="application/pdf"
    )

@router.get("/list", response_model=ReportListResponse)
async def list_reports(page: int = 1, page_size: int = 20, model_id: Optional[int] = None):
    """
    Liste des rapports générés (avec pagination)
    Optionnel: filtrer par model_id
    """
    # TODO: Récupérer rapports depuis base de données
    # TODO: Implémenter pagination
    # TODO: Filtrer par model_id si fourni
    # TODO: Ordonner par date création DESC
    
    # Mock response pour développement
    mock_reports = [
        ReportItem(
            report_id="rpt_123_1640995200",
            model_id=123,
            report_type="compliance",
            status="completed",
            created_at=datetime.now().replace(hour=datetime.now().hour - 2),
            completed_at=datetime.now().replace(hour=datetime.now().hour - 1),
            file_size_mb=2.4,
            download_url="/api/reports/download/rpt_123_1640995200"
        )
    ]
    
    return ReportListResponse(
        reports=mock_reports,
        total_count=1,
        page=page,
        page_size=page_size
    )

@router.delete("/{report_id}", response_model=ReportDeleteResponse)
async def delete_report(report_id: str):
    """
    Supprimer un rapport et son fichier PDF
    """
    # TODO: Vérifier que rapport existe
    # TODO: Vérifier permissions utilisateur
    # TODO: Supprimer fichier PDF du disque
    # TODO: Supprimer entrée base de données
    
    return ReportDeleteResponse(
        report_id=report_id,
        status="deleted",
        message="Rapport supprimé avec succès"
    )