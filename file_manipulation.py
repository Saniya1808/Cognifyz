import string

def count_words(file_path):
    word_counts = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
                words = line.lower().split()
                for word in words:
                    word_counts[word] = word_counts.get(word, 0) + 1
        
        sorted_words = sorted(word_counts.items())  # Sort alphabetically
        
        print("Word Count Results:")
        for word, count in sorted_words:
            print(f"{word}: {count}")
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = "Futureofcsestudents.txt"  # Change this to your actual file path
count_words(file_path)
