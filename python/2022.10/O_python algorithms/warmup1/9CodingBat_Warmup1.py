# http://codingbat.com/python
#1CodingBat_Warmup1.py


# Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged.

# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# not_string('not bad') → 'not bad'

def not_string(str):
  y = ('not ' + str)
  try:
    if str[0] == 'n' and str[1] == 'o' and str[2] == 't' and str[3] == ' ':
      return str
    else:
      return y
  except:
    if 'not' in str:
      return str
    else:
      return y