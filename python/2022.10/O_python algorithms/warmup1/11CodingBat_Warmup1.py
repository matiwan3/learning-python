'''
Given a string, return a new string where the first and 
last chars have been exchanged.
'''
# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

def front_back(str):
  str_len = len(str)

  
  if str_len > 2:
    first_let = str[0]
    last_let = str[-1]
    middle = str[1:-1]
    new_str = last_let + middle + first_let
    return new_str
  elif str_len == 2:
    first_let = str[0]
    second_let = str[-1]
    string_swap = second_let + first_let
    return string_swap
  else:
    return str

#Alternative solution
# def front_back(str):
#   if len(str) <= 1:
#     return str
  
#   mid = str[1:len(str)-1]  # can be written as str[1:-1]
  
#   # last + mid + first
#   return str[len(str)-1] + mid + str[0]