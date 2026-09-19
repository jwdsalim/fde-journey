print("--- 1. FOR LOOP DEMO (Batch Data Processing) ---")

# Maan lijiye aapke paas bank customers ki loan files ka collection hai
loan_files = ["Sameer_PAN.pdf", "Salary_Slip.pdf", "Tax_Return.xlsx", "Bank_Statement.csv"]
for index, file in enumerate(loan_files, start=1):
    # enumerate() ka use index aur item dono ko ek sath nikalne ke liye hota hai
    print(f"Processing File #{index}: {file}")
    if file.endswith(".xlsx"):
        print("-> WARNING: Excel file format detected. Scanning formatting...")
print("\n--- 2. WHILE LOOP DEMO (AI Token Stream Simulation) ---")

# Jab AI response stream hota hai, jab tak stop token nahi milta loop chalta hai
max_tokens_allowed = 1000
tokens_used = 200

# Loop tab tak chalega jab tak threshold exceed nahi hota
while tokens_used < max_tokens_allowed:
    print(f"Streaming chunks... Current Tokens: {tokens_used}")
    # Tokens ko badhana (C# ke tokens_used += 150; ki tarah)
    tokens_used += 200
    
    # Break statement check
    if tokens_used == 800:
        print("-> [System Alert]: Target context window optimal. Stopping stream safely.")
        break
print("--- Loop Execution Completed ---")

