# api_schemas/compliance.py (nouveau fichier)
from pydantic import BaseModel
from datetime import datetime
from typing import List

class BiasDetection(BaseModel):
    detected: bool
    severity: str                     # "low" | "medium" | "high"
    affected_groups: List[str]        # ["age", "gender"]
    bias_score: float                 # 0.0 à 1.0

class ComplianceAnalysisResponse(BaseModel):
    model_id: str
    eu_ai_act_classification: str     # "HIGH_RISK" | "LIMITED_RISK" | "MINIMAL_RISK"
    compliance_score: float           # 0.0 à 100.0
    bias_analysis: BiasDetection
    requirements: List[str]           # ["human_oversight_required", "audit_trail_mandatory"]
    analysis_timestamp: datetime
    status: str                       # "completed" | "failed"
    test_datasets_used: List[str]     # ["adult_income.csv", "synthetic_banking.csv"]
    total_test_cases: int | None   # Nombre de cas testés


class ComplianceStatusResponse(BaseModel):
    model_id: str
    analysis_status: str              # "pending" | "processing" | "completed" | "failed"
    progress_percentage: int          # 0 à 100
    estimated_completion: datetime | None
    last_updated: datetime
    error_message: str | None

class GetAnalysisResultsParams(BaseModel):
    analysis_id: str | None 
    analysis_date: str | None 
    test_datasets: str | None 
    latest: bool 
    include_metadata: bool = False
    