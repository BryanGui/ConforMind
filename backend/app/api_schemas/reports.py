# api_schemas/reports.py
from pydantic import BaseModel
from datetime import datetime
from typing import Literal, Optional
from enum import Enum

# ==================== ENUMS ====================

class ReportType(str, Enum):
    COMPLIANCE = "compliance"
    BIAS_ANALYSIS = "bias_analysis"
    FULL_AUDIT = "full_audit"
    RISK_ASSESSMENT = "risk_assessment"

# ==================== SCHEMAS PYDANTIC ====================

class ReportOptions(BaseModel):
    include_bias_analysis: bool = True
    include_recommendations: bool = True
    executive_summary: bool = True
    detailed_metrics: bool = False
    language: Literal["fr", "en"] = "fr"
    template_style: Literal["corporate", "technical", "executive"] = "corporate"

class ReportRequest(BaseModel):
    report_type: ReportType
    options: ReportOptions = ReportOptions()

class ReportGenerationResponse(BaseModel):
    report_id: str
    status: Literal["queued", "processing", "completed", "failed"]
    model_id: int
    report_type: str
    estimated_completion_time: datetime
    message: str

class ReportItem(BaseModel):
    report_id: str
    model_id: int
    report_type: str
    status: Literal["queued", "processing", "completed", "failed"]
    created_at: datetime
    completed_at: Optional[datetime] = None
    file_size_mb: Optional[float] = None
    download_url: Optional[str] = None

class ReportListResponse(BaseModel):
    reports: list[ReportItem]
    total_count: int
    page: int
    page_size: int

class ReportStatusResponse(BaseModel):
    report_id: str
    status: Literal["queued", "processing", "completed", "failed"]
    progress_percent: int
    current_step: str
    error_message: Optional[str] = None
    download_url: Optional[str] = None

class ReportDeleteResponse(BaseModel):
    report_id: str
    status: str
    message: str