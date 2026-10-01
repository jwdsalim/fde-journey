print("--- 🤖 DAY 22: ENTERPRISE AI OOPs ARCHITECTURE 🤖 ---")

class AIServiceAgent:
    """Enterprise-grade Wrapper Client Class for AI Models (C# Class Style)"""
    
    # 1. Constructor Implementation (C# public AIServiceAgent())
    def __init__(self, model_name: str, base_url: str, api_key: str):
        self.model_name = model_name   # Public Attribute
        self.base_url = base_url       # Public Attribute
        
        # Private Attribute: C# private string _apiKey ki tarah. 
        # Iske aage '__' lagane se yeh class ke bahar direct access nahi ho sakta.
        self.__api_key = api_key       
        
        print(f"-> Instance created for model: '{self.model_name}' safely.")

    # 2. Public Instance Method (C# Public Method)
    # Dhyan dein: Pehla parameter 'self' likhna compulsory hai
    def execute_prompt(self, prompt: str) -> str:
        print(f"\n[Routing API Request] via gateway: {self.base_url}")
        print(f"[Authenticating] Using masked token key: {self.__api_key[:5]}******")
        
        # Data Processing Simulation
        simulated_response = f"AI Response for '{prompt}' processed successfully by {self.model_name}."
        return simulated_response

    # 3. Getter Method for Private Variable (Encapsulation)
    def get_secure_mask(self) -> str:
        return f"HIDDEN_KEY_LEN_{len(self.__api_key)}"


# ==========================================
# EXECUTION WORKFLOW (Object Creation)
# ==========================================

# Object instantiate karna (C# ke 'new AIServiceAgent(...)' ki tarah, par Python mein 'new' keyword nahi lagta)
gpt_agent = AIServiceAgent(
    model_name="gpt-4o", 
    base_url="https://openai.com", 
    api_key="sk-proj-NETCORE9YEARSEXPERT12345"
)

# Public attributes ko direct access karna
print(f"Target Endpoint Model: {gpt_agent.model_name}")

# Method call karna
response = gpt_agent.execute_prompt("Analyze banking loan ledger dataset.")
print(f"Output received: {response}")

# --- SECURITY TESTING (Private Variable Check) ---
try:
    # Yeh line error degi kyunki __api_key private hai
    print(gpt_agent.__api_key)
except AttributeError as err:
    print(f"\n❌ [Encapsulation Security Pass]: Direct private access blocked! Details: {err}")
    # Sahi tarika getter tool use karna hai
    print(f"-> Safe Getter Access: {gpt_agent.get_secure_mask()}")

print("\n--- OOPs Architecture Verification Complete ---")
