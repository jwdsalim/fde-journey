from dataclasses import dataclass
from typing import Dict, Any, List, Optional

print("--- 🗺️ DAY 31: ENTERPRISE REST API ARCHITECTURE ROUTER 🗺️ ---")

# ==========================================
# 1. DATABASE RECORD MODEL (DTO Container Match)
# ==========================================
@dataclass
class AIModelResource:
    id: int
    name: str
    tier: str
    max_tokens: int


# Mock Database Ledger storing corporate AI instances
MODEL_DATABASE: Dict[int, AIModelResource] = {
    1: AIModelResource(id=1, name="gpt-4o", tier="Premium", max_tokens=128000),
    2: AIModelResource(id=2, name="claude-3.5-sonnet", tier="Premium", max_tokens=200000),
    3: AIModelResource(id=3, name="gpt-4o-mini", tier="Standard", max_tokens=128000)
}


# ==========================================
# 2. SEMANTIC REST ENDPOINT DISPATCHER
# ==========================================
class MockRESTEngine:
    """Simulates how enterprise Web API Controllers parse requests stateless-ly."""
    
    def dispatch_request(self, method: str, resource_path: str, body: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        print(f"\n[REST HTTP GATEWAY]: Intercepted {method} request at '{resource_path}'")
        
        # Split path parameters to mimic real URL routing engines
        path_segments = resource_path.strip("/").split("/")
        
        # Validate Base URL Contract: Expecting /api/v1/models
        if len(path_segments) < 3 or path_segments[0] != "api" or path_segments[1] != "v1" or path_segments[2] != "models":
            return {"status_code": 404, "response": {"error": "Endpoint route registry not found."}}

        # URL Pattern Match 1: GET /api/v1/models (Fetch Complete Collection)
        if method == "GET" and len(path_segments) == 3:
            all_records = [resource.__dict__ for resource in MODEL_DATABASE.values()]
            return {"status_code": 200, "response": {"total_count": len(all_records), "data": all_records}}

        # URL Pattern Match 2: GET /api/v1/models/{id} (Fetch Specific Element)
        elif method == "GET" and len(path_segments) == 4:
            try:
                resource_id = int(path_segments[3])
                if resource_id in MODEL_DATABASE:
                    return {"status_code": 200, "response": MODEL_DATABASE[resource_id].__dict__}
                return {"status_code": 404, "response": {"error": f"Resource with ID {resource_id} not found."}}
            except ValueError:
                return {"status_code": 400, "response": {"error": "Invalid Path Parameter: ID must be numeric."}}

        # URL Pattern Match 3: POST /api/v1/models (Create / Add New Entity)
        elif method == "POST" and len(path_segments) == 3:
            if not body or "name" not in body or "tier" not in body:
                return {"status_code": 400, "response": {"error": "Bad Request Payload: Required data fields missing."}}
            
            new_id = max(MODEL_DATABASE.keys()) + 1
            new_resource = AIModelResource(
                id=new_id, 
                name=body["name"], 
                tier=body["tier"], 
                max_tokens=body.get("max_tokens", 4096)
            )
            MODEL_DATABASE[new_id] = new_resource
            return {"status_code": 201, "response": {"message": "Resource created successfully", "resource": new_resource.__dict__}}

        # Default fallback for un-mapped HTTP verbs
        return {"status_code": 405, "response": {"error": f"HTTP Method '{method}' is restricted on this endpoint."}}


# ==========================================
# ARCHITECTURAL ROUTING VERIFICATION PIPELINE
# ==========================================

api_controller = MockRESTEngine()

# Scenario A: GET Request to read the whole model array ledger
result_collection = api_controller.dispatch_request(method="GET", resource_path="/api/v1/models")
print(f"-> Status Received: {result_collection['status_code']} OK\n-> Payload: {result_collection['response']}")

# Scenario B: GET Request with an ID parameter to read a specific component instance
result_single = api_controller.dispatch_request(method="GET", resource_path="/api/v1/models/2")
print(f"-> Status Received: {result_single['status_code']} OK\n-> Payload: {result_single['response']}")

# Scenario C: POST Request to ingest a new model definition configuration into db ledger
new_model_payload = {"name": "gemini-1.5-pro", "tier": "Premium", "max_tokens": 1000000}
result_create = api_controller.dispatch_request(method="POST", resource_path="/api/v1/models", body=new_model_payload)
print(f"-> Status Received: {result_create['status_code']} Created\n-> Payload: {result_create['response']}")

print("\n--- REST API Structural Framework Validation Passed ---")
