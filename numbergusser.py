import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))
    
    if lower_bound >= upper_bound:
        print("Invalid range. The upper bound must be greater than the lower bound.")
        return
    
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Guess the number: "))
            attempts += 1
            
            if guess < lower_bound or guess > upper_bound:
                print("Out of bounds! Try again within the given range.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()
