import random

print("--- AI GATEWAY FAULT TOLERANCE SIMULATION ---")

def call_azure_openai_api():
    """Ek mockup function jo randomly cloud network issues generate karta hai"""
    # 0 se 2 ke beech random number generate karein
    trigger_error = random.choice([0, 1, 2]) 
    
    if trigger_error == 1:
        raise TimeoutError("Azure Gateway Timeout: Request took longer than 15 seconds.")
    elif trigger_error == 2:
        raise ValueError("Invalid Parameter: 'temperature' must be between 0.0 and 2.0.")
    return "SUCCESS: AI Response data successfully generated from Azure GPT-4o."

# --- Main Try/Except System ---
try:
    print("Initiating connection to Azure Cloud AI Foundation...")
    api_response = call_azure_openai_api()

# 1. Specific Error A (C# catch specific exception)
except TimeoutError as timeout_ex:
    print(f"[RETRY LOGIC CHOSEN]: {timeout_ex}")
    print("-> Status: Running fallback request route to backup datacenter...")

# 2. Specific Error B
except ValueError as val_ex:
    print(f"[REJECTING REQUEST]: {val_ex}")
    print("-> Status: Bad Request payload found. Skipping system execution.")

# 3. Generic Error Handler (C# generic Exception ex)
except Exception as global_ex:
    print(f"[CRITICAL FAILURE]: Unexpected System Crash. Details: {global_ex}")

# 4. ELSE Block (Sirf Python mein hota hai - Runs ONLY if code is error-free)
else:
    print(f"Data Pipeline Clear! Response: {api_response}")

# 5. FINALLY Block (C# finally - Hamesha chalega chaho error aaye ya na aaye)
finally:
    print("Resource Cleanup Status: Closing active HTTP sockets and updating audit ledger.")
