from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def clear(clear_lines=10):
    for _ in range(clear_lines):
        print("")

def start_game():
    clear()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")


def set_difficulty():
    if input("Choose a difficulty. Type 'easy' or 'hard': ") == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def check_answer(guess, answer):
    if guess > answer:
        print("Too high.")
        return False
    elif guess < answer:
        print("Too low")
        return False
    else:
        print(f"You got it! The answer was {answer}")
        return True


def run_game():
    start_game()
    secret_number = randint(1, 100)
    remaining_tries = set_difficulty()
    win = False
    while not win and remaining_tries > 0:
        print(f"You have {remaining_tries} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        remaining_tries -= 1
        win = check_answer(guess, secret_number)
    if not win:
        print("You've run out of guesses, you lose.")
    if input("Type 'y' to try again or anything else to exit: ") == "y":
        run_game()


# main
run_game()