from pydantic import BaseModel, Field, ValidationError, EmailStr
from typing import List, Optional

print("--- 🛡️ DAY 33: ENTERPRISE DATA VALIDATION WITH PYDANTIC 🛡️ ---")

# ==========================================
# 1. ENTERPRISE VALIDATION SCHEMA (C# DTO Class)
# ==========================================
class AIOrchestratorConfigDTO(BaseModel):
    """
    Strict Data Transfer Object enforcing security rules before processing AI prompts.
    Matches C# Data Annotations / Model Validation engine rules.
    """
    # Required text string with absolute minimum length constraint
    client_prompt: str = Field(
        ..., 
        min_length=5, 
        max_length=1000, 
        description="The core instruction matrix for the active LLM."
    )
    
    # Optional field with strict value boundary ranges (Greater than or Equal / Less than or Equal)
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    
    # Integer constraints targeting billing tokens infrastructure
    max_tokens: int = Field(default=2000, gt=0, le=4096)
    
    # Nested arrays validation framework
    system_directives: List[str] = Field(default_factory=list)
    
    # Advanced metadata payload tracking email parameter contract
    # Note: Requires email-validator module, falls back to normal typing evaluation here
    developer_email: str = Field(..., pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")


# ==========================================
# EXECUTION VALIDATION RUNTIME MATRIX
# ==========================================

# --- SCENARIO A: 100% VALID PAYLOAD (Data Parsing Match) ---
print("\n[Scenario A]: Injecting Perfect Configuration Data JSON...")

valid_json_data = {
    "client_prompt": "Analyze banking ledger risk matrix vectors.",
    "temperature": 1.2,
    "max_tokens": 1500,
    "system_directives": ["SECURE_TUNNEL", "PII_SHIELD_ACTIVE"],
    "developer_email": "sameer.khan@enterprise.com"
}

# Parsing data object directly (C# Model Binding execution match)
config_instance = AIOrchestratorConfigDTO(**valid_json_data)
print("-> Status: Validation PASSED successfully.")
print(f"-> Parsed Object Context: {config_instance}")
print(f"-> Extracted Target Key Prompt: '{config_instance.client_prompt}'")


# --- SCENARIO B: CORRUPTED ATTACK PAYLOAD (Validation Failure Test) ---
print("\n[Scenario B]: Threat Testing - Injecting Invalid Constraint Data Matrix...")

corrupted_json_data = {
    "client_prompt": "Short", # Fails min_length constraint if length < 5 (Will catch if modified)
    "temperature": 5.5,       # Fails constraints limit (Must be <= 2.0)
    "max_tokens": -50,        # Fails validation constraint (Must be > 0)
    "developer_email": "invalid_email_format" # Fails regex validation pattern rule
}

try:
    # Attempting to parse bad structure to trigger automatic guardrail exception
    invalid_instance = AIOrchestratorConfigDTO(**corrupted_json_data)
except ValidationError as validation_err:
    print(f"❌ [Pydantic Guard]: Request blocked! Handled {validation_err.error_count()} structural data errors:")
    
    # Extracting precise JSON schema context error messages loops
    for error in validation_err.errors():
        field_location = " -> ".join(map(str, error["loc"]))
        error_msg = error["msg"]
        print(f"   * Field Violation Layer [{field_location}]: {error_msg}")

print("\n--- Pydantic Validation Infrastructure Pipeline Pass ---")
