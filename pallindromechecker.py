def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]


text = input("Enter a string to check if it's a palindrome: ")


if is_palindrome(text):
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")
