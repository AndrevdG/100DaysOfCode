# Import choice from the random module
from random import choice
import art
import game_data

def clear(clear_lines=10):
    for _ in range(clear_lines):
        print("")

# pick random item from list that is not the already selected item
def get_item_from_data(pick_not):
    selection = []
    while selection == [] or selection == pick_not:
        selection = choice(game_data.data)
    return selection


# Clear screen and write data
def write_screen(option_a, option_b, score):
    clear()
    print(art.logo)
    if not score == 0:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {option_a['name']}, a {option_a['description']} from {option_a['country']}\n")
    print(art.vs)
    print(f"Against B: {option_b['name']}, a {option_b['description']} from {option_b['country']}\n")


# Check answer
def check_result(higher, lower):
    if higher['follower_count'] > lower['follower_count']:
        return True
    else:
        return False


# Start game and display logo
def game():
    score = -1
    # Pick random item from list as 'A'
    option_a = get_item_from_data([])
    run_game = True
    while run_game:
        # Increase score (first time from -1 to 0)
        score += 1
        # Pick random item from the list as 'B'
        option_b = get_item_from_data(option_a)
        # Clear and update the screen
        write_screen(option_a, option_b, score)
        # Ask player who has more followers
        higher = input("Who has more followers? Type 'A' or 'B': ").lower()
        if higher == 'a':
            run_game = check_result(option_a, option_b)
        elif higher == 'b':
            run_game = check_result(option_b, option_a)
        else:
            # If player enters invalid choice, game fails
            run_game = False
        option_a = option_b
    clear()
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {score}")


game()