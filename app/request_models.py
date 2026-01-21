from pydantic import BaseModel

class SeverityItem(BaseModel):
    AESEV:str
    N:int

class SafeStats(BaseModel):
    total_sub: int
    subjects_having_ae:int
    subjects_having_sae:int
    severity:list[SeverityItem]

class SafeSummaryRequest(BaseModel):
    arm_filter:str
    age_filter:str
    teae_bool:bool
    stats:SafeStats
