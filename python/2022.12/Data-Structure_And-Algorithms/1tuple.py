"""
Python tuples are similar to lists but Tuples are immutable in nature i.e. once created it cannot be modified. Just like a List, a Tuple can also contain elements of various types.
In Python, tuples are created by placing a sequence of values separated by ‘comma’ with or without the use of parentheses for grouping of the data sequence. 
Note: To create a tuple of one element there must be a trailing comma. For example, (8,) will create a tuple containing 8 as the element.
"""

Tuple = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple)

list1 = [1,2,4,5,6]
print("\nTuple using List: ")
Tuple = tuple(list1)

print("First element of tuple")
print(Tuple[0])

print("\nLast element of tuple")
print(Tuple[-1])

print("\nThird last element of tuple")
print(Tuple[-3])
