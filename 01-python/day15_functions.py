print("--- 1. BASIC FUNCTION DEMO ---")

# Ek simple calculate cost function
def calculate_token_cost(tokens: int, rate_per_token: float = 0.0002) -> float:
    """Yeh function AI tokens ki cost calculate karta hai (Type hints ke sath)"""
    return tokens * rate_per_token


standard_cost=calculate_token_cost(1200)
print(f"Standard API Cost: ${standard_cost} ")

print("\n--- 2. ADVANCE FUNCTION DEMO (*args aur **kwargs) ---")


#========================================================
# AI System Orchestrator jo dynamically configurations accept karta hai
def initialize_ai_pipeline(system_name, *fallback_models, **model_settings):
    print(f"Main System Initialized: {system_name}")
    
    # 1. *args ka upyog (Tuple ki tarah print hota hai)
    if fallback_models:
        print("-> Backup Models Registered:")
        for model in fallback_models:
            print(f"   - {model}")
            
    # 2. **kwargs ka upyog (Dictionary ki tarah handle hota hai)
    print("-> Applying Model Configurations:")
    for key, value in model_settings.items():
        print(f"   - {key.upper()}: {value}")


# Function Call: Alag-alag tarike se settings bhejna
initialize_ai_pipeline(
    "Primary-Gateway",                  # system_name (Position Argument)
    "gpt-4-mini", "claude-3-haiku",     # *fallback_models (Kitne bhi strings - *args)
    temperature=0.7,                    # \
    max_tokens=2000,                    #  |-- **model_settings (Key-Value pairs - **kwargs)
    top_p=0.9,                          #  |
    is_secure=True                      # /
)