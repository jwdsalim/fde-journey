from fastapi import FastAPI
from pydantic import BaseModel, Field
import uvicorn
from fastapi.responses import RedirectResponse

print("--- 🧠 DAY 32: FASTAPI DEEP ARCHITECTURE UNDER THE HOOD 🧠 ---")

# 1. FastAPI Initialize kiya (C# -> var app = WebApplication.Create();)
app = FastAPI(
    title="FDE Enterprise AI Gateway",
    version="1.0.0"
)

# ==========================================
# 2. DATA BINDING MODEL (C# Strongly-Typed DTO Layout)
# ==========================================
class AIInferenceRequestDTO(BaseModel):
    """Pydantic model that acts as an automated security validation guard."""
    prompt: str = Field(description="The core text instruction for the LLM model.")
    max_tokens: int = Field(default=1000, ge=1, le=4000, description="Token range strict validation.")
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)


# ==========================================
# 3. HTTP ACTION ROUTING (C# Minimal API Map Endpoint Layout)
# ==========================================

# --- ENDPOINT 1: GET REQUEST ---
@app.get("/api/v1/health")
def get_infrastructure_health():
    """Stateless health checkpoint mapping."""
    print("\n[FastAPI Core]: Intercepted GET /api/v1/health request pipeline.")
    return {
        "status": "HEALTHY",
        "hosting_engine": "Uvicorn ASGI Server",
        "dotnet_developer_status": "Learning Python Fast"
    }


# --- ENDPOINT 2: POST REQUEST ---
@app.post("/api/v1/inference")
def execute_ai_inference(payload: AIInferenceRequestDTO):
    """Receives auto-validated JSON payloads and executes core business logic."""
    print("\n[FastAPI Core]: Intercepted POST /api/v1/inference pipeline.")
    print(f"[Pydantic Guard]: Validation Passed! Parsed object address registered.")
    
    # Strongly-typed variables memory object se read karna (Bilkul payload.Property ki tarah)
    client_prompt = payload.prompt
    token_limit = payload.max_tokens
    
    # Internal Logic Matrix Simulation
    simulated_cost = (len(client_prompt) * 0.0002) + (token_limit * 0.0005)
    
    print(f"[Log Matrix]: Calculated Token Cost Billing Tier: ${simulated_cost:.4f}")
    
    return {
        "transaction_status": "SUCCESS",
        "processed_prompt": client_prompt,
        "token_allowance_allocated": token_limit,
        "invoice_usd": round(simulated_cost, 4)
    }

# Advanced Framework Bootstrapper: Isse file ko direct Play Button se bhi host kiya ja sakta hai
if __name__ == "__main__":
    uvicorn.run("day32_fastapi:app", host="127.0.0.1", port=8000, reload=True)


# Jab koi direct root URL (/) par aayega, toh hum use auto-redirect kar denge Swagger par
@app.get("/")
def redirect_to_swagger():
    """C# RedirectToActionResult matching logic - Forces main page to open docs."""
    print("[Redirect Router]: Root hit! Redirecting client directly to Swagger UI Docs...")
    return RedirectResponse(url="/docs")