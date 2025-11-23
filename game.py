class Game:
    def __init__(self, secret_word: str):
        self.secret_word = secret_word
        self.guesses = set()
        self.attempts = 0
        self.max_attempts = 5
        self.wins = 0
        self.losses = 0
    
    def reset_game(self, secret_word: str):
        self.secret_word = secret_word
        self.guesses = set()
        self.attempts = 0

    def set_secret_word(self, new_word):
        self.secret_word = new_word
    
    def add_guess(self, char):
        self.guesses.add(char)
        self.attempts += 1
    
    def check_win(self) -> bool:
        return (set(self.secret_word) - self.guesses) == set()
    
    def check_loss(self) -> bool:
        return self.attempts > self.max_attempts

    def update_attempts(self):
        self.attempts = len(self.guesses - set(self.secret_word))
    
    def get_incorrect_guesses(self) -> str:
        incorrect_guesses = ""
        for char in self.guesses - set(self.secret_word):
            incorrect_guesses += char + " "
        return incorrect_guesses