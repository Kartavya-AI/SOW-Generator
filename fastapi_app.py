from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import sys
import os
from dotenv import load_dotenv
from src.sow.crew import Sow

# Load environment variables from .env file
load_dotenv()

# Ensure GEMINI_API_KEY is set and used exclusively
gemini_api_key = os.getenv("GEMINI_API_KEY")
if gemini_api_key:
    os.environ["GEMINI_API_KEY"] = gemini_api_key

# Set default model to Gemini if not set
if not os.getenv("MODEL"):
    os.environ["MODEL"] = "gemini/gemini-2.5-flash-preview-05-20"

app = FastAPI(
    title="Scope of Work Generator API",
    description="API to generate Scope of Work documents using CrewAI",
    version="1.0.0"
)

class GenerateSowRequest(BaseModel):
    client: str = Field(..., example="Alice from BrandCo")
    contractor: str = Field(..., example="Bob from DevGuru")
    raw_description: str = Field(..., example="Develop a modern Shopify-based e-commerce site with responsive design, payment gateway integration, SEO, and product listing features.")
    current_year: Optional[str] = Field(default_factory=lambda: str(datetime.now().year))

class GenerateSowResponse(BaseModel):
    sow_content: str

@app.get("/status", summary="Health check endpoint")
async def status():
    return {"status": "ok"}

@app.get("/status/health", summary="Health check endpoint")
async def status():
    checks = {
        "GEMINI_API_KEY": bool(os.getenv("GEMINI_API_KEY")),
        "SERPER_API_KEY": bool(os.getenv("SERPER_API_KEY")),
        "MODEL": bool(os.getenv("MODEL")),
    }

    # Overall status: ok only if all required configs are present
    overall = all(checks.values())

    return {
        "status": "ok" if overall else "error",
        "configuration": checks
    }

@app.post("/generate-sow", response_model=GenerateSowResponse, summary="Generate Scope of Work document")
async def generate_sow(request: GenerateSowRequest):
    inputs = {
        "Client": request.client,
        "Contractor": request.contractor,
        "raw_description": request.raw_description,
        "current_year": request.current_year,
    }
    try:
        result = Sow().crew().kickoff(inputs=inputs)
        sow_text = getattr(result, "raw", None) or str(result)

        return GenerateSowResponse(sow_content=sow_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating Scope of Work: {str(e)}")
