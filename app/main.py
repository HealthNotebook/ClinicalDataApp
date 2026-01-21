from fastapi import FastAPI
from app.request_models import SafeSummaryRequest
from app.llm_client import generate_summary
from fastapi import HTTPException

app = FastAPI()

@app.post("/generate-safety-summary")
def generate_safety_summ(payload : SafeSummaryRequest):
    try:
        summary = generate_summary(payload)
        return {"summary":summary}
    except:
        # Token exhausted / API failure / timeout
        raise HTTPException(
            status_code=503,
            detail="LLM service temporarily unavailable"
        )
