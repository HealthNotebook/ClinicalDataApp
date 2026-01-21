from fastapi import FastAPI
# from app.request_models import SafeSummaryRequest
# from app.llm_client import generate_summary

from request_models import SafeSummaryRequest
from llm_client import generate_summary

from fastapi import HTTPException
import os
import uvicorn
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

# Hugging Face uses 7860 by default. 
# If "PORT" isn't set (like on your local PC), it defaults to 8000.
port = int(os.environ.get("PORT", 7860))
    
# Use 0.0.0.0 to allow external traffic (like your Shiny app)
uvicorn.run(app, host="0.0.0.0", port=port)