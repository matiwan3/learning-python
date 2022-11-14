'''
Given a string, return a new string where the first and 
last chars have been exchanged.
'''


# Given a string and a non-negative int n,
# return a larger string that is n copies of the original string.


# string_times('Hi', 2) → 'HiHi'
# string_times('Hi', 3) → 'HiHiHi'
# string_times('Hi', 1) → 'Hi'

def string_times(str, n):
  return n * str

#alternative
# def string_times(str, n):
#   result = ""
#   for i in range(n):  # range(n) is [0, 1, 2, .... n-1]
#     result = result + str  # could use += here
#   return result