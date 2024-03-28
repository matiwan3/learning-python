import random

unitClassNameArcher = 'Archer'
unitClassNameMag = 'Mag'
unitClassNameWarrior = 'Warrior'
unitClassNameNinja = 'Ninja'
unitClassNameGuardian = 'Guardian'

def classChooseInfo(unitClassName):
    print(f'\nYou chose: {unitClassName}')
    
def getStats(health, armor, strength, stamina, tool, gold):
    print(f'Current stats of your character: \nHealth: {health}\nArmor: {armor}\nStrength: {strength}\nStamina: {stamina}\nTool: {tool}\nGold: {gold}')
    

def welcomePrompt():
    print('---------------------------------------------')
    print('|        Welcome to prompt adventures       |')
    print('|        Version 0.1-ENG                    |')
    print('|        All rights reserved by matiwan     |')
    print('---------------------------------------------\n')

def unitChoose():
    chooseClass = input('Choose desired class: \n1. Archer\n2. Mag\n3. Warrior\n4. Ninja\n5. Guardian\nYour choice: ')
    if chooseClass == '1':
        unit = UnitArcher()
    elif chooseClass == '2':
        unit = UnitMag()
    elif chooseClass == '3':
        unit = UnitWarrior()
    elif chooseClass == '4':
        unit = UnitNinja()
    elif chooseClass == '5':
        unit = UnitGuardian()
    else:
        print('[SYSTEM] Invalid choice!')
        return 0
    return unit
        
class UnitArcher:
    def __init__(self):
        self.health = 5
        self.armor = 2
        self.strength = 3 
        self.stamina = 6
        self.tool = 'Bow'
        self.inventory = {}
        self.gold = random.randint(0,100)
        classChooseInfo(unitClassNameArcher)
        getStats(self.health, self.armor, self.strength, self.stamina, self.tool, self.gold)
        
    def getGold(self):
        print(f'Gold: {self.gold}')
        
class UnitMag:
    def __init__(self):
        classChooseInfo(unitClassNameMag)
    
class UnitWarrior:
    def __init__(self):
        classChooseInfo(unitClassNameWarrior)
    
class UnitNinja:
    def __init__(self):
        classChooseInfo(unitClassNameNinja)
        
class UnitGuardian:
    def __init__(self):
        classChooseInfo(unitClassNameGuardian)

def main():
    run = True
    while run: 
        welcomePrompt()
        unit = unitChoose()
        if unit == 0:
            break
        unit.getGold()
        run = False
    
if __name__ == '__main__':
    print('[SYSTEM] Starting the game...')
    main()
