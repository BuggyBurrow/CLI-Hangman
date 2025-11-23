import random

FILE = "top-1000-nouns.txt"

def get_random_word() -> str:
    ran_num = random.randrange(1, 1000)

    return read_nth_word_from_file(ran_num)

def read_nth_word_from_file(num: int) -> str:
    with open(FILE) as file:
        for _ in range(num):
            word = file.readline()
    
    return word.strip()
