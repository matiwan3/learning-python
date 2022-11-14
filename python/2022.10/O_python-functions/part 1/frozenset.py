# Frozen Set
# frozenset()

# Can be used as keys in dictionaries

lst = [1,2,3]
s = set(lst)
s.add(4)

print(s)

fs = frozenset(lst)
print(fs)