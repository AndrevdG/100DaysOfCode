import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

# win_matrix matches user_choice against computer_choice
# e.g. win_matrix[user_choice][computer_choice] -> d = draw, l = lose, w = win
win_matrix = [["d", "l", "w"], ["w", "d", "l"], ["l", "w", "d"]]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if 0 < user_choice < 3:
    print(choices[user_choice])
    computer_choice = random.randint(0, 2)
    print(choices[computer_choice])

    if win_matrix[user_choice][computer_choice] == "d":
        print("It's a draw!")
    elif win_matrix[user_choice][computer_choice] == "l":
        print("You lose!")
    else:
        print("You win! Yay!")
else:
    print("Illegal choice, you lose!")