# Get attr

class MyClass:
    def __init__(self, x):
        self.x = x
        
c = MyClass(10)
print(getattr(c, "x"))