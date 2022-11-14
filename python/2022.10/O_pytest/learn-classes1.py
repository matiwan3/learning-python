class Dog:
    
    def __init__(self, name):
        self.name = name
        self.tricks = []
        
    def add_tricks(self, trick):
        self.tricks.append(trick)
        
d = Dog('Fido')
e = Dog('Buddy')
d.add_tricks('roll over')
e.add_tricks('play dead')
print(d.tricks)

        
