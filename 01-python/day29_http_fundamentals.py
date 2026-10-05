from dataclasses import dataclass
from typing import Dict, Any, Union

print("--- 🌐 DAY 29: ENTERPRISE HTTP FUNDAMENTALS SIMULATOR 🌐 ---")

# ==========================================
# 1. HTTP RESPONSE CONTAINER (DTO Pattern Match)
# ==========================================
@dataclass(frozen=True)
class MockHTTPResponse:
    status_code: int
    status_phrase: str
    headers: Dict[str, str]
    body: Dict[str, Any]


# ==========================================
# 2. CORE GATEWAY ROUTER (Simulating Server Responses)
# ==========================================
def simulate_ai_gateway_request(http_method: str, payload_valid: bool, has_auth_token: bool) -> MockHTTPResponse:
    """Simulates how cloud API gateways evaluate HTTP Verbs and headers."""
    
    # Common standard headers
    response_headers = {"Content-Type": "application/json", "Server": "AzureOpenAI/Gateway"}

    # Guard Clause 1: Auth Validation (401 Unauthorized Check)
    if not has_auth_token:
        return MockHTTPResponse(
            status_code=401,
            status_phrase="Unauthorized",
            headers=response_headers,
            body={"error": "Authentication failed. Missing or invalid Bearer API Key Token."}
        )

    # Guard Clause 2: Payload Validation (400 Bad Request Check)
    if http_method == "POST" and not payload_valid:
        return MockHTTPResponse(
            status_code=400,
            status_phrase="Bad Request",
            headers=response_headers,
            body={"error": "Malformed JSON payload structure. Required 'prompt' field missing."}
        )

    # Success Flow based on Verbs
    if http_method == "GET":
        return MockHTTPResponse(
            status_code=200,
            status_phrase="OK",
            headers=response_headers,
            body={"active_models": ["gpt-4o", "claude-3.5-sonnet"], "status": "HEALTY"}
        )
        
    elif http_method == "POST":
        return MockHTTPResponse(
            status_code=201,
            status_phrase="Created",
            headers=response_headers,
            body={"id": "chat-9921", "choices": [{"text": "Hello Sameer! Execution Complete."}]}
        )
        
    else:
        return MockHTTPResponse(
            status_code=405,
            status_phrase="Method Not Allowed",
            headers=response_headers,
            body={"error": f"HTTP Method '{http_method}' is restricted on this AI endpoint."}
        )


# ==========================================
# EXECUTION TESTING PIPELINE
# ==========================================

print("\n[Scenario A]: Sending a Valid POST Request (C# HttpClient.PostAsync Match)")
response_a = simulate_ai_gateway_request(http_method="POST", payload_valid=True, has_auth_token=True)
print(f"-> Response Status: {response_a.status_code} {response_a.status_phrase}")
print(f"-> Body JSON: {response_a.body}")

print("\n[Scenario B]: Threat/Security Test - Missing Token Auth Key")
response_b = simulate_ai_gateway_request(http_method="POST", payload_valid=True, has_auth_token=False)
print(f"-> Response Status: {response_b.status_code} {response_b.status_phrase}")
print(f"-> Body JSON: {response_b.body}")

print("\n[Scenario C]: Formatting Error Test - Sending Bad JSON Structure")
response_c = simulate_ai_gateway_request(http_method="POST", payload_valid=False, has_auth_token=True)
print(f"-> Response Status: {response_c.status_code} {response_c.status_phrase}")
print(f"-> Body JSON: {response_c.body}")

print("\n--- HTTP Fundamentals Architecture Verification Complete ---")
