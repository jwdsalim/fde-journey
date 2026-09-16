# --- TUPLE DEMO ---
# Configuration locks karne ke liye
model_config = ("gpt-4o", 0.7, 2000) # (Model, Temperature, MaxTokens)
print("Tuple value (Model Name):", model_config[0])

# Agar aap ise change karne ki koshish karenge toh Error aayega:
# model_config[1] = 0.5 # TypeError: 'tuple' object does not support item assignment


# --- SET DEMO ---
# Duplicate entries handle karne ke liye
user_queries = ["loan status", "apply loan", "loan status", "interest rate"]
unique_queries = set(user_queries)

# Duplicate value ("loan status") automatic gayab ho jayegi
print("Original List length:", len(user_queries)) # 4
print("Unique Set length:", len(unique_queries))   # 3
print("Unique Queries:", unique_queries)
