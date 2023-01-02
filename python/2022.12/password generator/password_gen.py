# password generator based on random lib
import random

lower_case = 'abcdefghijklmnoprstuwxyz'
upper_case = lower_case.upper()
numbers = '1234567890'
signs = '~!@#$%^&*()_+-={}|[]\:;<>,.?/'

combination = lower_case + upper_case + numbers + signs

# hardcode length of password
pass_length = 12
password="".join(random.sample(combination, pass_length))

print(password)