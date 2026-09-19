print("--- 1. STANDARD FOR LOOP WAY (Traditional) ---")

# Maan lijiye hamare paas AI response tokens ki ek raw list hai
token_logs = [150, 2400, 320, 4500, 95, 1200]

# Humein sirf un logs ko filter karna hai jo 1000 tokens se bade hain (High Cost Logs)
high_cost_logs = []
for tokens in token_logs:
    if tokens > 1000:
        high_cost_logs.append(tokens)
print("Traditional Way Output:", high_cost_logs)

#======================================================

print("\n--- 2. LIST COMPREHENSION WAY (C# LINQ Style) ---")
# Same logic ko sirf ek line mein likhenge
# Syntax rule: Pehle kya chahiye -> Fir loop -> Fir condition
smart_high_cost_logs = [tokens for tokens in token_logs if tokens > 1000]
print("List Comprehension Output:", smart_high_cost_logs)

#=======================================================

print("\n--- 3. DATA TRANSFORMATION DEMO (LINQ .Select() Style) ---")
# User queries ki strings ko clean karna aur upper case karna
raw_queries = ["  loan approval status ", "apply credit card", " check Balance  "]

# Har string se extra spaces hatana (.strip()) aur uppercase karna (.upper())
clean_queries = [query.strip().upper() for query in raw_queries]
print("Cleaned Enterprise Queries:")
for q in clean_queries:
    print(f"   - {q}")