def my_func(lst):
    result = sum((x for x in (y + 1 for y in lst)), 10)
    return result

numbers = [1,2,3,4,5]
print(my_func(numbers)) # 10

