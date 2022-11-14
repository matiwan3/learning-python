from random import randrange

unsorted_list = [randrange(10)
                 for _ in range(10)]
*sorted_list ,= unsorted_list
sorted_list.sort()
print(f"{unsorted_list = } ") 
print(f"{sorted_list = } ") 