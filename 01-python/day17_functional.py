print("--- 1. LAMBDA FUNCTION DEMO (Inline Logic) ---")

# C# ke fat arrow (=>) ki tarah ek single line anonymous function
# Syntax: lambda input_parameters: expression
calculate_tax = lambda amount: amount * 0.18

print(f"Tax for $500: ${calculate_tax(500)}")

#===================================================

print("\n--- 2. FILTER() DEMO (LINQ .Where() Equivalent) ---")
# Maan lijiye hamare paas corporate client queries ke token counts hain
token_logs = [450, 2200, 1500, 800, 3100, 950]

# filter() un items ko nikalta hai jo condition true karte hain
# Yeh lazy loading karta hai, isliye ise list() mein typecast karna padta hai
high_usage_logs = list(filter(lambda tokens: tokens > 1000, token_logs))
print("Filtered High Usage Logs (>1000 tokens):", high_usage_logs)

#===================================================

print("\n--- 3. MAP() DEMO (LINQ .Select() Equivalent) ---")
# map() har ek item par functions apply karke naya object banata hai
# Hum har high usage token log ko standard API rate ($0.0002 per token) se multiply karenge
api_costs = list(map(lambda tokens: tokens * 0.0002, high_usage_logs))
print("Calculated API Cost for High Logs ($):", api_costs)