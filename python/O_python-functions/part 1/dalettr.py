# Delete Attribute
# delattr()

class MyClass:
    def __init__(self, x):
        self.x = x
        
c = MyClass(10)

print(c.x)
delattr(c, "x")
print(c.x)