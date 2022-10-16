# https://www.programiz.com/python-programming/class

class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def calc_perimeter(self):
        perimeter = self.a + self.b + self.c
        return perimeter
        
t1 = Triangle(3,4,5)
print(t1.calc_perimeter())
        