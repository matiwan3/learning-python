'''
Find e to the Nth Digit - Just like the previous problem, but with e instead of π (pi).
Enter a number and have the program generate e up to that many decimal places.
Keep a limit to how far the program will go.
'''

import math
import cs50

decimal_number = cs50.get_int("Enter the number and I will print the pi with this number in decimal places(max 15): ")
# print(math.e)
e = '2.'
number = '718281828459045'
for i in number[:decimal_number]:
    e += i
print(e)
