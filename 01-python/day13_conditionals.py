# System Configuration Setup
token_count = 2500
user_role = "Premium"

print("--- AI Gateway Route Controller ---")# System Configuration Setup
token_count = 2500
user_role = "Premium"

print("--- AI Gateway Route Controller ---")

# 1. Multi-condition Logic Test
# Python mein curly braces {} nahi hote, sirf colon (:) aur indentation (4 spaces) hota hai
if token_count > 4000:
    print("ALERT: Request blocked! Token limit exceeded.")
elif token_count > 2000 and user_role != "Premium":
    print("WARNING: High token usage detected for standard user. Throttling applied.")
elif token_count > 2000 and user_role == "Premium":
    print("SUCCESS: High token request approved for Premium Tier.")
else:
    print("SUCCESS: Standard request processed immediately.")

# 2. Boolean Short-hand check
is_active_client = True
if is_active_client:
    print("System Access: GRANTED")
