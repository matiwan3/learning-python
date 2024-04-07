def procent_kwoty():
    print("Oblicza procent z danej kwoty")
    get_amount = int(input('[$] Kwota początkowa: ')) # 80
    get_percentage = int(input('[%] Procent kwoty: ')) # 5
    value = (get_percentage / get_amount) * 100
    print(f'{get_percentage}% z {get_amount}$ wynosi: {value}$')

def procent_składany():
    print('Oblicza procent składany')
    starting_balance = int(input('[$] Kwota początkowa: '))
    week_percentage_earn = int(input('[%] Procent jaki zarabiasz w tydzień: '))
    weeks_amount = int(input('[T] Przez ile tygodni będziesz zarabiał: '))
    
    final_balance = starting_balance

    for _ in range(weeks_amount):
        final_balance *= (1 + week_percentage_earn / 100)

    print(f'Mając {starting_balance}$ na początku, zarabiając {week_percentage_earn}% tygodniowo przez {weeks_amount} tygodni, osiągniesz końcową kwotę {final_balance:.2f}$')

# Wywołanie funkcji
procent_składany()
procent_kwoty()