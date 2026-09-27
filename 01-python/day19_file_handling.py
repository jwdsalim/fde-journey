import json
import os

print("--- 📂 ENTERPRISE FILE & JSON ARCHITECTURE DEMO 📂 ---")

# Files ke paths define karein
TEXT_LOG_PATH = "ai_audit_trail.txt"
JSON_DATA_PATH = "chat_history_metadata.json"

# ==========================================
# PART 1: Standard Text Writing & Reading (C# StreamWriter/Reader)
# ==========================================
print("\n[Step 1]: Writing streaming logs to plain text file...")

# 'w' means Write mode (overwrite). 'a' means Append mode.
with open(TEXT_LOG_PATH, "w", encoding="utf-8") as text_file:
    text_file.write("[AUDIT LOG - 2026-09-19]: AI Gateway initialized successfully.\n")
    text_file.write("[AUDIT LOG - 2026-09-19]: Request from user 'Sameer_Khan' processed via Azure OpenAI.\n")

print(f"-> Success: Logs written to {TEXT_LOG_PATH}")

# Text file read karna ('r' mode)
print("\n[Step 2]: Reading plain text log back from file...")
if os.path.exists(TEXT_LOG_PATH):
    with open(TEXT_LOG_PATH, "r", encoding="utf-8") as text_file:
        content = text_file.read()
        print("--- Text File Content ---")
        print(content.strip())
        print("-------------------------")


# ==========================================
# PART 2: JSON Serialization & Storage (C# System.Text.Json)
# ==========================================
print("\n[Step 3]: Serializing complex Dictionary to JSON file...")

# Simulation: LLM response data structured as a dictionary
ai_chat_response = {
    "session_id": "session_9942",
    "user": "Sameer Khan",
    "prompt": "Write a 1-page doc on FDE Workflow",
    "response_metadata": {
        "model": "gpt-4o",
        "tokens_used": 1450,
        "is_hallucination_detected": False
    }
}

# json.dump() dict ko direct file mein JSON banakar likh deta hai
# indent=4 lagane se JSON perfectly readable format (pretty print) mein save hota hai
with open(JSON_DATA_PATH, "w", encoding="utf-8") as json_file:
    json.dump(ai_chat_response, json_file, indent=4)

print(f"-> Success: Complex AI Metadata serialized into {JSON_DATA_PATH}")

# JSON file read aur parse karna (Deserialization)
print("\n[Step 4]: Parsing JSON file back into Python Dictionary...")
if os.path.exists(JSON_DATA_PATH):
    with open(JSON_DATA_PATH, "r", encoding="utf-8") as json_file:
        # json.load() JSON text file ko wapas Python dictionary mein badal deta hai
        parsed_data = json.load(json_file)
        
        # Dictionary ki tarah data extract karna
        print(f"-> Session ID Retrieved: {parsed_data['session_id']}")
        print(f"-> Target Model Extracted: {parsed_data['response_metadata']['model']}")
        print(f"-> Total Tokens Invoiced: {parsed_data['response_metadata']['tokens_used']}")

print("\n--- File Infrastructure Simulation Completed Safely ---")
