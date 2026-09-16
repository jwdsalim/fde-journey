# Python Code
age = 30             # int
name = "Sameer"      # str
salary = 85000.50    # float (Python mein double nahi hota, sab float hai)
isFDE = True         # bool (Dhyan rahe: True aur False ka 'T' aur 'F' Capital hota hai)


# Variables define karein
developer_name = "Jawed Salim"
years_of_exp = 9
is_ai_ready = False

# Type check karne ke liye type() function ka use hota hai (Jaise C# mein GetType() hota hai)
print(type(developer_name))  # Output: <class 'str'>
print(type(years_of_exp))    # Output: <class 'int'>
print(type(is_ai_ready))     # Output: <class 'bool'>

# Dynamic Typing Test: Ek variable ka type baad mein badal bhi sakta hai
test_var = 100
print("Pehle:", type(test_var))
test_var = "Ab main string hoon"
print("Baad mein:", type(test_var))
