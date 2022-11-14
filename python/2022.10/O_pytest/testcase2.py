######### PYTESTS #########

def addition(x):
    return 5+x

my_even_list = []
my_odd_list = []
my_list = []
my_dictionary = {}
my_tuple = ()
def simple_loop(my_even_list,my_odd_list):
    for num in range(1,51):
        if num % 2 == 0:
            my_even_list.append(num)
        else:
            my_odd_list.append(num)
    return my_even_list,my_odd_list

simple_loop(my_even_list,my_odd_list)
print(f'Evens: {my_even_list}\nOdds: {my_odd_list}')
print(type(my_dictionary))
print(type(my_list))
print(type(my_tuple))

# def test_addition():
    # assert twierdzenie !
    # assert addition(5) == 10

# def test_always_fails():
    # assert False