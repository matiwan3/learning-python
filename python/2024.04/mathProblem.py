BALLS = 777
def countBlackBalls():
    counter_7 = 0
    n = 1
    for x in range(0,BALLS):
        if (n == 2 or n == 3) and '7' in str(x):
            for num_index in range(0,len(str(x))):  
                if str(x)[num_index] == '7':
                    counter_7 += 1
        if n == 3:
            n = 1
            continue
        n += 1
    print(f"Count of all digits '7' used on black balls equals: {counter_7}")

countBlackBalls()