# Random Remarks
# Function defined outside the class

def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1
    
    def g(self):
        return 'hello world'
    
    h = g
    
################################################################################

class Bag:
    def __init__(self):
        self.data = []
        
    def add(self, x):
        self.data.append(x)
        
    def addtwice(self, x):
        self.add(x)
        self.add(x)