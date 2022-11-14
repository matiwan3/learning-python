#Made by MW 18.8.2022

print("=========================================\nWelcom to stock market position averager! \n=========================================\n")
number_of_positions = int(input("Tip: To input float number please use comma!\nEnter number of positions: "))

def calculate_it(nof):
    average_list = []
    amount = 0
    average_position = 0

    for x in range(0, nof):
        price = float(input("Enter price: "))
        amount = float(input("Enter amount: "))
        amount_check = amount + amount
        average_list.append(price * amount)

    result = 0
    for x in average_list:
        result += x

    average_position = result / amount_check

    print(f"Total amount: {amount_check}, Average position equals: {average_position}")
    return average_position  
#
calculate_it(number_of_positions)

