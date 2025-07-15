# routers/compliance.py (nouveau fichier)
from fastapi import APIRouter, HTTPException, Depends 
from app.api_schemas.compliance import ComplianceAnalysisResponse, BiasDetection,GetAnalysisResultsParams
from datetime import datetime
import glob



router = APIRouter(prefix="/api/compliance", tags=["EU AI Act Compliance"])

@router.post("/analyze/{model_id}", response_model=ComplianceAnalysisResponse)
async def analyze_model_compliance(model_id: str):
    """
    Lance l'analyse de conformité EU AI Act sur un modèle IA uploadé.
    
    Effectue classification automatique du risque, détection de biais et génère 
    la liste des exigences réglementaires. Sauvegarde les résultats en base
    pour consultation ultérieure. Retourne l'analyse complète au client.
    """
    
    # Vérifier que le modèle existe
    pattern = f"data/client_uploads/{model_id}_*"
    files = glob.glob(pattern)
    
    if not files:
        raise HTTPException(
            status_code=404, 
            detail=f"Model {model_id} not found"
        )
    
    # ================================================================
    # TODO PHASE 2: Appeler business_logic/compliance_engine.py
    # TODO PHASE 2: Appeler business_logic/bias_detector.py
    # ================================================================
    
    # Mock analysis pour l'instant
    mock_bias = BiasDetection(
        detected=True,
        severity="medium",
        affected_groups=["age", "gender"],
        bias_score=0.23
    )
    
    # Préparer résultats
    results = ComplianceAnalysisResponse(
        model_id=model_id,
        eu_ai_act_classification="HIGH_RISK",
        compliance_score=67.5,
        bias_analysis=mock_bias,
        requirements=[
            "human_oversight_required",
            "audit_trail_mandatory", 
            "risk_assessment_documented",
            "bias_mitigation_implemented"
        ],
        analysis_timestamp=datetime.now(),
        status="completed",
        test_datasets_used=[
            "adult_income.csv", 
            "synthetic_banking.csv"
        ],
        total_test_cases=2847
    )
    
    # ================================================================
    # TODO PHASE 2: Sauvegarder en base de données
    # save_to_database(model_id, results)
    # ================================================================
    
    return results



@router.get("/results/{model_id}", response_model=ComplianceAnalysisResponse)
async def get_compliance_results(
    model_id: str,
    params: GetAnalysisResultsParams = Depends()
) -> ComplianceAnalysisResponse:
    """
    Récupère les résultats d'une analyse de conformité spécifique.
    
    Permet de sélectionner quelle analyse récupérer par ID, date ou datasets utilisés.
    Par défaut retourne la plus récente analyse pour ce modèle.
    """
    
    # Vérifier que le modèle existe
    pattern = f"data/client_uploads/{model_id}_*"
    files = glob.glob(pattern)
    
    if not files:
        raise HTTPException(status_code=404, detail=f"Model {model_id} not found")
    
    # ================================================================
    # TODO PHASE 2: Récupérer selon params depuis base de données
    # if params.analysis_id:
    #     results = load_by_analysis_id(params.analysis_id)
    # elif params.analysis_date:
    #     results = load_by_date(model_id, params.analysis_date)
    # elif params.latest:
    #     results = load_latest_analysis(model_id)
    # ================================================================
    
    # Mock results (en attendant DB)
    mock_bias = BiasDetection(
        detected=True,
        severity="medium", 
        affected_groups=["age", "gender"],
        bias_score=0.23
    )
    
    return ComplianceAnalysisResponse(
        model_id=model_id,
        eu_ai_act_classification="HIGH_RISK",
        compliance_score=67.5,
        bias_analysis=mock_bias,
        requirements=[
            "human_oversight_required",
            "audit_trail_mandatory", 
            "risk_assessment_documented",
            "bias_mitigation_implemented"
        ],
        analysis_timestamp=datetime.now(),
        status="completed",
        test_datasets_used=[
            "adult_income.csv", 
            "synthetic_banking.csv"
        ],
        total_test_cases=2847
    )