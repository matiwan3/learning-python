# Filter
# filter()
# lambda - anonymous func
def filter_func(value):
    return value % 2 == 0

lst = [1,2,3,4,5,6,7,8,9,10]
evens = filter(lambda x: x % 2 == 0, lst)
evens_2 = filter(filter_func, lst)

print(evens)
print(evens_2)

print(list(evens))
print(list(evens_2))