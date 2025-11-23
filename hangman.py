from game import Game
from random_word import get_random_word
import sys

def main():
    game = Game(get_random_word())

    print(f"Welcome to Buggy Hangman.")
    
    while True:
        display_word(game)
        display_hangman(game)
        
        if game.check_win():
            print("You won!")
            print()
            game.wins += 1
            prompt_play_again(game)
            continue

        elif game.check_loss():
            print("You lost!")
            print()
            game.losses += 1
            prompt_play_again(game)
            continue

        game.add_guess(prompt_char())
        game.update_attempts()
        

def prompt_char () -> str:
    while True:
        user_input = input("Choose a letter: ")
        if user_input and user_input[0].isalpha():       
            return user_input[0].lower()

    
def prompt_play_again(game):
    while True:
        user_input = input("Would you like to play again? (y/n): ")
        if user_input and user_input[0].lower() == 'n':
            print()
            print_stats(game)
            print("Thank you for playing Buggy Hangman")
            sys.exit()
        elif user_input and user_input[0].lower() == 'y':
            game.reset_game(get_random_word())
            return


def display_word(game: Game):
    for char in game.secret_word:
        if char in game.guesses:
            print(f"{char}", end=" ")
        else:
            print("_", end=" ")
    print()


def display_hangman(game: Game):

    heads = ["😁", "🫠", "🙂", "😨", "😵", "💀", "🪦"]
    print(f"  {heads[game.attempts]}  ")
    match game.attempts:
        case 0:
            print()
            print()
        case 1:
            print("   |  ")
            print()
        case 2:
            print("  /|  ")
            print()
        case 3:
            print(r"  /|\ ")
            print()
        case 4:
            print(r"  /|\ ")
            print(r"    \ ")
        case 5:
            print(r"  /|\ ")
            print(r"  / \ ")
        case 6:
            print()


def print_stats(game: Game):
    print(f"You won {game.wins} time(s) and lost {game.losses} time(s)")

if __name__ == "__main__":
    main()