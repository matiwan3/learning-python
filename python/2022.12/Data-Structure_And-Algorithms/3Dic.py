"""
Python dictionary is an unordered collection of data that stores data in the format of key:value pair. It is like hash tables in any other language with the time complexity of O(1). Indexing of Python Dictionary is done with the help of keys. These are of any hashable type i.e. an object whose can never change like strings, numbers, tuples, etc. We can create a dictionary by using curly braces ({}) or dictionary comprehension.
"""

Dict = {'Name': 'Geeks', 1: [1,2,3,4]}
print("Creating Dictionary: ")
print(Dict)

# Accessing a element using key
print("Accessing a element using key: ")
print(Dict['Name'])

# accessing a element using get() method

print("Accessing a element using get: ")
print(Dict.get(1))

# creation using Dictionary comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict)