'''
Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.
'''

import cs50

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

number = cs50.get_int("Enter a number: ")

factors = prime_factors(number)
print(factors)