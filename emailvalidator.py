import re

def validate_email(email):
    """Validates an email address based on format rules."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    if re.match(pattern, email):
        return True
    return False

email = input("Enter an email address to validate: ")

if validate_email(email):
    print("Valid email address.")
else:
    print("Invalid email address.")
