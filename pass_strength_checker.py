import re

def check_password_strength(password):
    strength = 0
    remarks = ""
    
    # Check length
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    
    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    
    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    
    # Check for digits
    if re.search(r"\d", password):
        strength += 1
    
    # Check for special characters
    if re.search(r"[@$!%*?&]", password):
        strength += 1
    
    # Evaluate strength
    if strength >= 5:
        remarks = "Very Strong"
    elif strength == 4:
        remarks = "Strong"
    elif strength == 3:
        remarks = "Moderate"
    elif strength == 2:
        remarks = "Weak"
    else:
        remarks = "Very Weak"
    
    return f"Password Strength: {remarks}"

# Example usage
password = input("Enter your password: ")
print(check_password_strength(password))
