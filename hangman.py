def main():
    criminal_name = "Bob"

    print(f"Welcome to Buggy Hangman. Let's hang {criminal_name}")

    secret_word = "buggy"
    guesses = set()

def prompt_char () -> str:
    while True:
        user_input = input("Choose a letter: ")
        if user_input and user_input[0].isalpha():
            return user_input[0].lower()


def display_word(word: str, guesses: list):

    for char in word:
        if char in guesses:
            print(f"{char}", end=" ")
        else:
            print("_", end=" ")
    
    print()

if __name__ == "__main__":
    main()