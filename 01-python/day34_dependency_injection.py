from fastapi import FastAPI, Depends, Header, HTTPException
from typing import Dict, Generator
import uvicorn

print("--- 🏗️ DAY 34: ENTERPRISE FASTAPI DEPENDENCY INJECTION 🏗️ ---")

app = FastAPI(title="FDE Secured AI DI Gateway Pipeline", version="1.0.0")

# ==========================================
# 1. DEPENDENCY A: DATABASE INSTANCE LIFECYCLE (C# AddScoped DatabaseContext)
# ==========================================
class MockDatabaseConnection:
    def __init__(self):
        self.connection_string = "Server=AzureAI-DB-Prod;Catalog=ComplianceLedger;"
    
    def log_transaction(self, message: str):
        print(f"   [SQL Database Ledger]: Writing payload track -> {message}")


# Dependency Generator Function (C# using block lifecycle pattern)
def get_database_session() -> Generator[MockDatabaseConnection, None, None]:
    """Simulates C# Scoped DbContext lifecycle. Creates connection and closes post HTTP response."""
    db_instance = MockDatabaseConnection()
    print("\n[DI Engine]: 🟢 SQL DB Connection Session Established safely.")
    try:
        # yield ka matlab hai object runtime code ko hand-over kar diya gaya hai
        yield db_instance
    finally:
        # HTTP response return hone ke theek BAAD yeh block automatic trigger hoga (C# Dispose check)
        print("[DI Engine]: 🔴 SQL DB Connection Session Disposed/Closed cleanly.")


# ==========================================
# 2. DEPENDENCY B: SECURITY GUARD CORPLOGIC (C# [Authorize] Policy alternate)
# ==========================================
def verify_api_compliance_token(x_api_key: str = Header(..., description="Corporate secret key header token check.")) -> str:
    """Strict architectural guard policy that intercepts headers before hitting database layer."""
    print(f"[DI Engine]: 🛡️ Auditing incoming security header token: {x_api_key[:5]}******")
    
    # Strict core logic verification pass bounds
    if x_api_key != "FDE_SECURE_CLOUD_NETCORE_KEY_9982":
        raise HTTPException(status_code=401, detail="Infrastructure Guard: Unauthorized Access Key.")
        
    return "COMPLIANCE_PASSED"


# ==========================================
# 3. HTTP ENDPOINT WITH PARAMETER LEVEL DI INJECTION
# ==========================================
@app.post("/api/v1/secure-inference", tags=["Production AI Routes"])
def execute_enterprise_inference(
    prompt: str,
    db: MockDatabaseConnection = Depends(get_database_session), # Injected Scope
    security_status: str = Depends(verify_api_compliance_token)  # Injected Guard
):
    """
    Core Controller Business Logic.
    FastAPI will automatically resolve dependencies left-to-right before executing this method block.
    """
    print(f"[Core Endpoint]: Authentication matrix verified status: {security_status}")
    print(f"[Core Endpoint]: Routing user prompt to target models pipeline execution layer.")
    
    # Database connection context object use karna (C# resolved Context variable match)
    db.log_transaction(f"Processed valid AI instance payload for prompt: '{prompt[:20]}...'")
    
    return {
        "status": "INFERENCE_SUCCESSFUL",
        "compliance_tier": security_status,
        "payload_echo": prompt
    }

# Root redirect utility for immediate Swagger access
from fastapi.responses import RedirectResponse
@app.get("/")
def home():
    return RedirectResponse(url="/docs")

if __name__ == "__main__":
    uvicorn.run("day34_dependency_injection:app", host="127.0.0.1", port=8000, reload=True)
