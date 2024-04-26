def procent_kwoty():
    print("Obliczam procent z danej kwoty")
    get_amount = int(input('[$] Kwota początkowa: ')) # 80
    get_percentage = int(input('[%] Procent kwoty: ')) # 5
    value = (get_percentage / get_amount) * 100
    print(f'{get_percentage}% z {get_amount}$ wynosi: {value:.2f}$')

def procent_składany():
    print('Obliczam procent składany')
    starting_balance = int(input('[$] Kwota początkowa: '))
    week_percentage_earn = int(input('[%] Procent jaki zarabiasz w tydzień: '))
    weeks_amount = int(input('[T] Przez ile tygodni będziesz zarabiał: '))
    
    final_balance = starting_balance

    for _ in range(weeks_amount):
        final_balance *= (1 + week_percentage_earn / 100)

    print(f'Mając {starting_balance}$ na początku, zarabiając {week_percentage_earn}% tygodniowo po {weeks_amount} tygodniach zarobisz: {final_balance:.2f}$')

def main():
    user_choice = int(input("Wybierz akcje. \n1. Procent danej kwoty\n2. Procen składany\nWybór: "))
    if user_choice == 1:
        procent_kwoty()
    elif user_choice == 2:
        procent_składany()
    else:
        return 0
        
if __name__ == "__main__":
    main()