import sys

def bankaccount():
    password = "123"
    counter = 0
    mat_balance = 189569
    zbi_balance = 232569
    mac_balance = 344569
    eus_balance = 456569
    system_run = True
    name_list = ['Mateusz','Zbigniew','Maciej','Eustachy']
    print("Central Bank Reserves ©️")
    while system_run:
        
        name = input("Enter your name: ")
        enter_password = input("Enter a password: ")
        account_run = True
        
        if (enter_password == password) and ( name in name_list): 
            print(f"Access granted! Welcome {name}\n")
            while account_run:
                if name == 'Mateusz':
                    print(f"Your account balance: {mat_balance} $\nTo deposite write - D\nTo withdraw write - W\nTo quit write - Q")
                    key_entered = input("Enter a key: ").upper()
                    if key_entered == 'Q':
                        sys.exit()
                    elif key_entered == 'D':
                        deposite_amount = int(input("How much would you like to deposite?: "))
                        confirm = input("Are you sure? Y/N: ").upper()
                        if confirm == 'Y':
                            mat_balance += deposite_amount
                        elif confirm =='N':
                            pass
                    elif key_entered == 'W':
                        withdraw_amount = int(input("How much would you like to withdraw?: "))
                        confirm = input("Are you sure? Y/N: ").upper()
                        if confirm == 'Y':
                            if withdraw_amount > mat_balance:
                                print("Too large amount to withdraw! Try again")    
                            else:
                                mat_balance -= withdraw_amount
                        elif confirm =='N':
                            pass
                elif name == 'Zbigniew':
                    print(f"Your account balance: {zbi_balance} $\nTo deposite write - D\nTo withdraw write - W\nTo quit write - Q")
                    key_entered = input("Enter a key: ").upper()
                    if key_entered == 'Q':
                        sys.exit()
                    elif key_entered == 'D':
                        deposite_amount = int(input("How much would you like to deposite?: "))
                        confirm = input("Are you sure? Y/N: ").upper()
                        if confirm == 'Y':
                            zbi_balance += deposite_amount
                        elif confirm =='N':
                            pass
                    elif key_entered == 'W':
                        withdraw_amount = int(input("How much would you like to withdraw?: "))
                        confirm = input("Are you sure? Y/N: ").upper()
                        if confirm == 'Y':
                            if withdraw_amount > zbi_balance:
                                print("Too large amount to withdraw! Try again")    
                            else:
                                zbi_balance -= withdraw_amount
                        elif confirm =='N':
                            pass
                elif name == 'Maciej':
                    print(f"Your account balance: {mac_balance} $\nTo deposite write - D\nTo withdraw write - W\nTo quit write - Q")
                    key_entered = input("Enter a key: ").upper()
                    if key_entered == 'Q':
                        sys.exit()
                    elif key_entered == 'D':
                        deposite_amount = int(input("How much would you like to deposite?: "))
                        confirm = input("Are you sure? Y/N: ").upper()
                        if confirm == 'Y':
                            mac_balance += deposite_amount
                        elif confirm =='N':
                            pass
                    elif key_entered == 'W':
                        withdraw_amount = int(input("How much would you like to withdraw?: "))
                        confirm = input("Are you sure? Y/N: ").upper()
                        if confirm == 'Y':
                            if withdraw_amount > mac_balance:
                                print("Too large amount to withdraw! Try again")    
                            else:
                                mac_balance -= withdraw_amount
                        elif confirm =='N':
                            pass
                elif name == 'Eustachy':
                    print(f"Your account balance: {eus_balance} $\nTo deposite write - D\nTo withdraw write - W\nTo quit write - Q")
                    key_entered = input("Enter a key: ").upper()
                    if key_entered == 'Q':
                        sys.exit()
                    elif key_entered == 'D':
                        deposite_amount = int(input("How much would you like to deposite?: "))
                        confirm = input("Are you sure? Y/N: ").upper()
                        if confirm == 'Y':
                            eus_balance += deposite_amount
                        elif confirm =='N':
                            pass
                    elif key_entered == 'W':
                        withdraw_amount = int(input("How much would you like to withdraw?: "))
                        confirm = input("Are you sure? Y/N: ").upper()
                        if confirm == 'Y':
                            if withdraw_amount > eus_balance:
                                print("Too large amount to withdraw! Try again")    
                            else:
                                eus_balance -= withdraw_amount
                        elif confirm =='N':
                            pass
        else:
            print("Access denied \n")
            counter += 1
            if counter == 3:
                print("account has been blocked!")
                break
if __name__ == "__main__":
    bankaccount()

