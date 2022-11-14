# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.


# Syntax: lambda arguments : expression
x = lambda a : a + 10
print(x(5))

y = lambda x,b : x * b
print(y(7, 5))

z = lambda a, b : a * b
print(z(5, 6))

k = lambda a, b, c : a + b + c
print(k(5, 6, 2))

# WHy use lambda ? 
# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myfunc(n):
    return lambda a : a * n

# create a doubling fucntion
mydoubler = myfunc(2) # set 'n'

# output 11(a) * 2(n) == 22
print(mydoubler(11)) # pass 'a' in

# Creating doubling and tripling function at once !!
# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# print(mydoubler(11))
# print(mytripler(11))
# Use lambda functions when an anonymous function is required for a short period of time.