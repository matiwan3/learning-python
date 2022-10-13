class Person:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight
        
    def bmi(self):
        BMI = (self.weight / (self.height**2)) * 10000
        BMI.round(2)
        return BMI



Jan = Person("Jan", 180, 82)

Veronica = Person("Veronica", 168, 56)

print(Jan.bmi())