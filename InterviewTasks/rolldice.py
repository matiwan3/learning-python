import random

def roll_dice():
    x = random.randint(1,6)
    return x
run = True
while run:
    
    user_choice = input("Press any key to roll or type 'quit' to exit... ")
    if user_choice == "quit":
        run = False
    else:
        print(roll_dice())

