def fibonacci_sequence(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return
    fib_sequence = [0, 1]  # Initialize with first two terms
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    print("Fibonacci Sequence:", fib_sequence[:n])

# Get user input
try:
    terms = int(input("Enter the number of terms: "))
    fibonacci_sequence(terms)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
