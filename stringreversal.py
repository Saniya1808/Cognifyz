def reverse_string(user_input: str) -> str:
    reversed_str = "".join([user_input[i] for i in range(len(user_input) - 1, -1, -1)])
    return reversed_str

user_text = input("Enter a string to reverse:")
print("Reversed String:", reverse_string(user_text))
