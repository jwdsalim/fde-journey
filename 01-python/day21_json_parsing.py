import json

print("--- 🧠 DAY 21: ENTERPRISE AI PAYLOAD PARSER 🧠 ---")

# Simulation: Yeh ek raw JSON string hai jo kisi AI API response se aayi hai
raw_api_response_str = """
{
    "id": "chatcmpl-a1b2c3d4",
    "object": "chat.completion",
    "created": 1727431200,
    "model": "gpt-4o-2026-05-10",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "Loan approval criteria met. Risk index is low."
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 1050,
        "completion_tokens": 250,
        "total_tokens": 1300
    }
}
"""

# ==========================================
# STEP 1: JSON String to Python Dict (Deserialization)
# ==========================================
print("\n[Step 1]: Parsing raw JSON string using json.loads()...")
# json.loads() -> 's' stands for String. Yeh string ko dict mein badalta hai.
payload = json.loads(raw_api_response_str)
print(f"-> Successfully converted to type: {type(payload)}")


# ==========================================
# STEP 2: Extracting Nested Data Safely (C# LINQ to JSON Style)
# ==========================================
print("\n[Step 2]: Extracting nested elements safely...")

# Core details nikalna
model_used = payload.get("model", "Unknown")
# choices list ke andar se pehle element ka message content nikalna
ai_answer = payload["choices"][0]["message"]["content"]
total_tokens = payload["usage"]["total_tokens"]

print(f"   - Model Used: {model_used}")
print(f"   - AI Response Text: '{ai_answer}'")
print(f"   - Total Tokens: {total_tokens}")


# ==========================================
# STEP 3: Modifying Payload & Converting Back to JSON (Serialization)
# ==========================================
print("\n[Step 3]: Adding internal audit flags and updating payload...")

# Payload dictionary mein naye metadata fields add karna
payload["audit_metadata"] = {
    "parsed_by": "Sameer_Khan_FDE",
    "is_approved_for_billing": True,
    "calculated_cost_usd": total_tokens * 0.0002
}

# json.dumps() -> Dict ko wapas valid clean JSON String mein badal deta hai
# ensure_ascii=False lagane se special characters ya unicode text kharab nahi hota
updated_json_str = json.dumps(payload, indent=4, ensure_ascii=False)

print("\n--- Modified JSON Payload (First few lines) ---")
# Sirf starting ki 15 lines print karke check karne ke liye string slicing
print("\n".join(updated_json_str.splitlines()[:15]))
print("...")
print("-----------------------------------------------")
