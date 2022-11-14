guess = 1

while True:
    num = input("Please guess the number (between 0-100: ")
    try:
        num = int(num)
    except:
        print('Invalid number, please uess again.')
        continue
    
    if num < 45:
        print('Your guess was under.')
    elif num > 45: #Hard codded
        print('Your guess was over.')
    else:
        break
    
    guess += 1
    
print(f'You guessed it in {guess} guesses')