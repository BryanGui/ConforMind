from pydantic import BaseModel
from typing import Dict, Any
from datetime import datetime


class HealthResponse(BaseModel):
    status: str
    timestamp: datetime
    message: str

class ComponentStatus(BaseModel):
    name: str
    status: str  # "OK" | "ERROR" | "WARNING"
    details: str | None = None
    response_time_ms: float | None = None

class DetailedHealthResponse(BaseModel):
    status: str
    timestamp: datetime
    components: list[ComponentStatus]
    system_info: Dict[str, Any]

class VersionResponse(BaseModel):
    api_version: str
    environment: str
    build_timestamp: datetime
    uptime_seconds: float