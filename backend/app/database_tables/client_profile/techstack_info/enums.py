from enum import Enum

class InfrastructureType(str, Enum):
    CLOUD = "cloud"
    ON_PREMISE = "on_premise" 
    HYBRID = "hybrid"