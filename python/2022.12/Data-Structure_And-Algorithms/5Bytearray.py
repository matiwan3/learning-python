"""
Python Bytearray gives a mutable sequence of integers in the range 0 <= x < 256.
"""
# Creating bytearray
a = bytearray((12, 8, 25, 2))
print("Creating Bytearray: ")
print(a)

# accessing elements
print("\nAccessing e\Elements: ", a[1])

# modify elements
a[1] = 3
print("\nAfter Modifying:")
print(a)

# Appending elements
a.append(30)
print("\nAfter Adding Elements:")
print(a)