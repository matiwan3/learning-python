BALLS = 777
def countBlackBalls():
    counter_7 = 0
    index = 1
    for x in range(0,BALLS):
        if (index == 2 or index == 3) and '7' in str(x):
            for y in range(0,len(str(x))):  
                if str(x)[y] == '7':
                    counter_7 += 1
        if index == 3:
            index = 1
            continue
        index += 1
    print(f"Count of all '7' used on black balls equals: {counter_7}")

countBlackBalls()