#Rock scissors paper game
import random


def player_input():
    p_guess = input("Player: ")
    return p_guess
    
def bot_choice():
    bot_guess = random.randint(1,3)
    if bot_guess == 1:
        print("Bot: rock")
        return 'R'
    elif bot_guess == 2:
        print("Bot: scissors")
        return 'S'
    elif bot_guess == 3:
        print("Bot: paper")
        return 'P'
    

def replay():
    choice_list = ['Y', 'N']
    choice = input("Do you want to play again ? Y/N: ")
    while choice not in choice_list:
        choice = input("Do you want to play again ? Y/N: ")
    return choice == 'Y' #True



while True:
    p_score = 0
    b_score = 0
    start_game = input("Welcome to rock scissors paper game!\nTo start the game press 'S' to exit press 'E': ")
    game_on = True
    while start_game not in ['S','E']:
        start_game = input("To start the game press 'S' to exit press 'E': ")
    if start_game == 'S':
        while game_on:
            list = ["rock", "scissors", "paper"]
            print("Please type rock, scissors or paper: ")
            pi = player_input() 
            while pi not in list:
                player_input()
                pi = player_input()
            bc = bot_choice()
            if ((bc == 'R') and (pi == 'rock')):
                print("Tie!")
            elif ((bc == 'S') and (pi == 'scissors')):
                print("Tie!")
            elif ((bc == 'P') and (pi == 'paper')):
                print("Tie!")
            elif ((bc == 'S') and (pi == 'rock')):
                p_score += 1
                print(f"YOU WIN!!!\nYour score is: {p_score}\nBot score is: {b_score}")
            elif ((bc == 'P') and (pi == 'scissors')):
                p_score += 1
                print(f"YOU WIN!!!\nYour score is: {p_score}\nBot score is: {b_score}") 
            elif ((bc == 'R') and (pi == 'paper')):
                p_score += 1
                print(f"YOU WIN!!!\nYour score is: {p_score}\nBot score is: {b_score}")
            else:
                b_score += 1
                print(f"You loseee!\nYour score is: {p_score}\nBot score is: {b_score}")

            if not replay():
                game_on = False
    else:
        break

