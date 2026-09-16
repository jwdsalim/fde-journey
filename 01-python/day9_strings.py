# 1. Multi-line Prompt Example
system_prompt = """You are an expert FDE Assistant.
Your task is to help a senior .NET developer learn Python.
Current User: Jawed Salim"""

# 2. F-String (Formatting)
tokens = 250
log_message = f"AI Response generated successfully using {tokens} tokens."
print(log_message)

# 3. String Methods & Slicing
text = "Enterprise AI Automation"
print(text.upper())          # ENTERPRISE AI AUTOMATION
print(text.startswith("Ent")) # True
print(text[0:10])            # Output: Enterprise (Pehle 10 characters)
