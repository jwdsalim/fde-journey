# 1. Dictionary Create Karna (AI Metadata Model)
customer_profile = {
    "id": 101,
    "name": "Sameer Khan",
    "skills": [".NET Core", "Microservices", "Python"], # Value mein list bhi ho sakti hai
    "tokens_used": 1500
}

# 2. Value Access Kaise Karein?
# Tareeka A: Direct Bracket (Agar key nahi mili toh Error aayega)
print("Customer Name:", customer_profile["name"])

# Tareeka B: .get() Method (Best Practice - Key na milne par 'None' return karega, crash nahi hoga)
email = customer_profile.get("email", "Email nahi mili!") 
print("Email Status:", email)
        
# 3. Value Update aur Add Karna
customer_profile["tokens_used"] = 1850    # Existing value update ki
customer_profile["role"] = "Senior FDE"   # Nayi key-value pair add ki

# 4. Dictionary ke saare Keys aur Values par Loop chalana
print("\n--- Complete Profile Metadata ---")
for key, value in customer_profile.items():
    print(f"{key.upper()}: {value}")
