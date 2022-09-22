'''
Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
'''
import cs50


def fib_seq(n,task):
    n1, n2 = 0,1
    count = 0
    if task == 1:
        for i in range(n):
            pass

    elif task == 2:
        while count < n:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
            print(n2)
    else:
        print("wrong number!")


task = cs50.get_int("Fibbo to the number(1) or to the Nth number(2): ")
number = cs50.get_int("Enter a number: ")

fib_seq(number,task)
