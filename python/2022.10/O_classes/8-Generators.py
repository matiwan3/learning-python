# Generators are a simple and powerful tool for creating iterators. 
# They are written like regular functions but use the yield statement whenever they want to return data.
# Each time next() is called on it, the generator resumes where it 
# left off (it remembers all the data values and which statement was last executed). 
# An example shows that generators can be trivially easy to create:

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
        
>>> for char in reverse('golf'):
...     print(char)
...
f
l
o
g