'''
Find PI to the Nth Digit - Enter a number and have the program generate π (pi) up to that many decimal places.
Keep a limit to how far the program will go.
'''
# pip install math-pi
# pip install cs50

import math_pi
import cs50

decimal_number = cs50.get_int("Enter the number and I will print the pi with this number in decimal places: ")
print(math_pi.pi(b=decimal_number))

