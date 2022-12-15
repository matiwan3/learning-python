""" The -> (arrow) is used to annotate the return value for a function in Python 3.0 or later. 
It does not affect the program but is intend to be consumed by other users or 
libraries as documentation for the function. """


def return_int(num1) -> int:
    simple_string = "aaa"
    sum_of_nums = num1 + 2
    return sum_of_nums

def return_string(my_name) -> str:
    greet = f'hello, my name is {my_name}'
    return greet

def return_none(empty_list) -> None:
    for x in range(len(empty_list)):
        print(f'{empty_list[x]} at index {x}')
        
    
    
print(return_int(5))
print(return_string('Mat'))
print(return_none([1,5,7,65,34,12,3,8]))