import requests
from requests.exceptions import HTTPError

print("--- 📡 DAY 30: ENTERPRISE LIVE REQUESTS PIPELINE 📡 ---")

# ==========================================
# PART 1: HTTP GET REQUEST (C# GetAsync Match)
# ==========================================
print("\n[Step 1]: Fetching sample data ledger via HTTP GET...")
TARGET_GET_URL = "https://typicode.com"

try:
    # Requests dispatcher call (Connection timeout limit set to 5 seconds)
    response = requests.get(TARGET_GET_URL, timeout=5)
    
    # Strict Status Check Control: Agar code 4xx ya 5xx hua toh yeh direct exception raise karega
    # C# equivalent: response.EnsureSuccessStatusCode();
    response.raise_for_status()
    
    # Response JSON extraction (C# JsonConvert.DeserializeObject)
    data = response.json()
    print(f"-> Success Status: {response.status_code} OK")
    print(f"-> Retrieved Record Title: '{data.get('title')}'")

except HTTPError as http_err:
    print(f"❌ HTTP Error Caught: {http_err}")
except Exception as global_err:
    print(f"❌ Connection Crash: {global_err}")


# ==========================================
# PART 2: HTTP POST REQUEST (C# PostAsync Match)
# ==========================================
print("\n[Step 2]: Dispatching AI payload ledger via HTTP POST...")
TARGET_POST_URL = "https://typicode.com"

# Mock payload structure representing AI metadata transaction logs
payload = {
    "title": "AI_Gateway_Audit_Log",
    "body": "System status: HEALTHY. User: Sameer_Khan_FDE. Tokens: 3500.",
    "userId": 101
}

custom_headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "Authorization": "Bearer SK_PROJ_PRODUCTION_NETCORE_AUDIT_KEY_9921"
}

try:
    # POST transaction trigger using direct 'json=' parameter for automatic encoding
    post_response = requests.post(TARGET_POST_URL, json=payload, headers=custom_headers, timeout=5)
    post_response.raise_for_status()
    
    returned_payload = post_response.json()
    print(f"-> Success Status: {post_response.status_code} Created")
    print(f"-> Generated Entity ID from Remote Host: {returned_payload.get('id')}")
    print(f"-> Confirmed Body Payload: {returned_payload.get('body')}")

except HTTPError as post_http_err:
    print(f"❌ POST Transaction Aborted: {post_http_err}")

print("\n--- Live Requests Infrastructure Pipeline Complete ---")
