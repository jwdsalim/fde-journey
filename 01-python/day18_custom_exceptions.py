# 1. Custom Exception Class Define Karein
# C# ke 'class MyException : Exception' ki tarah base Exception class se inherit karein

class InsufficientAIWalletBalanceError(Exception):
    """Exception tab raise hogi jab user ke paas AI run karne ke liye पर्याप्त tokens na hon."""
    def __init__(self, current_balance, required_cost, message="AI Wallet Balance Insufficient."):
        self.current_balance = current_balance
        self.required_cost = required_cost
        # Base class Exception ke constructor ko call karna (C# ke : base(message) ki tarah)
        super().__init__(f"{message} Available: ${current_balance}, Required: ${required_cost}")

#=============================================================

# 2. Business Logic Function (AI Gateway Core)
def process_llm_request(user_wallet_balance: float, prompt_length: int) -> str:
    # Maan lijiye AI cost formula hai: per character $0.01 cost hai
    estimated_cost = prompt_length * 0.01
    
    print(f"[Gateway Analysis]: Cost calculated: ${estimated_cost:.2f} | User Wallet: ${user_wallet_balance:.2f}")
    
    if user_wallet_balance < estimated_cost:
        # C# ke 'throw new CustomException()' ki tarah 'raise' ka use karein
        raise InsufficientAIWalletBalanceError(user_wallet_balance, estimated_cost)
        
    return "SUCCESS: AI Model executed safely. Token logs updated."

#===========================================================================

# 3. Main Try/Except Implementation
try:
    print("--- ⚙️ STARTING ENTERPRISE AI GATEWAY TRANSACTION ⚙️ ---")
    # Simulation: User ke paas sirf $5.00 hain par prompt bohot bada hai ($8.00 ki cost wala)
    api_result = process_llm_request(user_wallet_balance=5.00, prompt_length=800)
    print(api_result)

# 4. Custom Error ko specific Catch karna (C# catch block)
except InsufficientAIWalletBalanceError as wallet_err:
    print(f"\n❌ [CRITICAL AGENT ALERT]: {wallet_err}")
    print(f"-> Missing Amount: ${wallet_err.required_cost - wallet_err.current_balance:.2f}")
    print("-> Action Required: Redirecting customer to Stripe Payment gateway endpoint...")

except Exception as global_ex:
    print(f"Unexpected infrastructure crash: {global_ex}")

finally:
    print("--- ⚙️ GATEWAY TRANSACTION COMPLETE ⚙️ ---")
