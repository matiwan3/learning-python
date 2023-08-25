
class legoSniper():
    def __init__(self, health, ammo, hit_num):
        self.health = health
        self.ammo = ammo
        self.hit_num = hit_num
        
    def attack(number):
        attack_list = [4,5,6]
        if number in attack_list:
            return number
        else: 
            return 0
        

def game():
    run = True
    while True:
        player_choice = input("Welcome in CHARARMY game. \nPress S to start\nPress E to close")
        if player_choice == "S":
            pass
        
        elif player_choice == "E":
            run = False
        else:
            print('Wrong choice. Try again')