# http://codingbat.com/python
#
#Given an int n, return the absolute difference between n and 21,
#except return double the absolute difference if n is over 21.

def diff21(n):
  if n<= 21:
    return abs(21-n)
  else:
    return abs((21-n)*2)