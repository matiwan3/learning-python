import random

unitClassNameArcher = 'Łucznik'
unitClassNameMag = 'Mag'
unitClassNameWarrior = 'Wojownik'
unitClassNameNinja = 'Zabójca'
unitClassNameGuardian = 'Strażnik'

def classChooseInfo(unitClassName):
    print(f'\nYou chose: {unitClassName}')
    
def getStats(health, armor, strength, stamina, tool, gold):
    print(f'Statystyki postaci: \nZdrowie: {health}\nZbroja: {armor}\nSiła: {strength}\nWytrzymałość: {stamina}\nBroń: {tool}\nZłoto: {gold}')
    

def welcomePrompt():
    print('---------------------------------------------')
    print('|       Witaj w konsolowych przygodach      |')
    print('|       Version 0.1-PL                      |')
    print('|       Wszystkie prawa zastrzeżone matiwan |')
    print('---------------------------------------------\n')

def unitChoose():
    chooseClass = input('Wybierz klasę: \n1. Łucznik\n2. Mag\n3. Wojownik\n4. Zabójca\n5. Strażnik\Twój wybór: ')
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
        print('[SYSTEM] Niepoprawny wybór!')
        return 0
    return unit
        
class UnitArcher:
    def __init__(self):
        self.health = 5
        self.armor = 2
        self.strength = 3 
        self.stamina = 6
        self.tool = 'Drewniany łuk'
        self.inventory = {}
        self.gold = random.randint(0,100)
        classChooseInfo(unitClassNameArcher)
        getStats(self.health, self.armor, self.strength, self.stamina, self.tool, self.gold)
        
    def getGold(self):
        print(f'Złoto: {self.gold}')
        
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
    print('[SYSTEM] Włączanie gry...')
    main()
