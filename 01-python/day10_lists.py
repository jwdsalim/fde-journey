# 1. List Create aur Modify karna
ai_tools=["FastAPI","Semantic Kernal", "LangChain"]
print("Initial List:", ai_tools)

# Naya item add karna (C# ke .Add() ki tarah)
ai_tools.append("Azure Open AI")

# Specific index par item access karna
print("Pehla tool:", ai_tools[0])   # Output: FastAPI

# 2. List Slicing (Data engineering mein bohot use hota hai)
# Agar hazaaron records mein se sirf pehle 2 chahiye hon:
top_two_tools = ai_tools[0:2]
print("Top 2 Tools:", top_two_tools)

# 3. List clear/remove karna
ai_tools.remove("LangChain")
print("Update ke baad:", ai_tools)