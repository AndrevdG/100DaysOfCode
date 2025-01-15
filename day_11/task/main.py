from art import logo
import random

def clear(lines=10):
    for _ in range(lines):
        print("")

def deal_card(hand):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    hand["cards"].append(card)
    hand["total"] += card
    if hand["total"] == 21 and len(hand["cards"]) == 2:
        hand["total"] = 0
    if hand["total"] > 21 and hand["cards"].count(11) > 0:
        index = hand["cards"].index(11)
        hand["cards"][index] = 1
        hand["total"] -= 10

    return hand


def init_hand():
    hand = {
        "total": 0,
        "cards": [],
    }
    for _ in range(2):
        hand = deal_card(hand)
    return hand


def pick_winner(player, computer):
    print(f"\tYour final hand: {player['cards']}, final score: {player['total']}")
    print(f"\tComputer's final hand: {computer['cards']}, final score: {computer['total']}")
    if player["total"] > 21 or computer["total"] > 21:
        if player["total"] > 21:
            print("you went over, you lose 😤")
        else:
            print("Opponent went over, you win! 😁")
    elif player["total"] == computer["total"]:
        print("Draw! 🙃")
    elif computer["total"] == 0 or player["total"] == 0:
        if computer["total"] == 0 and player["total"] == 0:
            print("Draw! Everyone blackjack! 🙃")
        elif computer["total"] == 0:
            print("Opponent wins, blackjack! 😤")
        else:
            print("you win, blackjack! 😁")
    elif player["total"] > computer["total"]:
        print("You have the higher score. You win! 😁")
    else:
        print("Opponent has the higher score. Opponent  wins 😤")


def play_game():
    if input("Do you want to play a game of Blackjack? Type 'y' anything else will exit game: ").lower() != 'y':
        return
    clear()
    print(logo)
    player = init_hand()
    computer = init_hand()
    players_move = True
    while players_move and 0 < player["total"] <= 20:
        print(f"\tYour cards: {player['cards']}, current score: {player['total']}")
        print(f"\tComputer's first card: {computer['cards'][0]}")
        if input("Type 'y' to get another card, type anything else to pass. ") == "y":
            player = deal_card(player)
        else:
            players_move = False
    while computer["total"] != 0 and computer["total"] < 17 and 0 < player["total"] <= 21:
        computer = deal_card(computer)
    pick_winner(player, computer)
    play_game()


# main
play_game()