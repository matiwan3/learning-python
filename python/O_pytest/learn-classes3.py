class Person:
    
    
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight
        
    def bmi(self):
        calc_BMI = (self.weight / (self.height**2)) * 10000
        BMI = round(calc_BMI,2)
        return BMI



Jan = Person("Jan", 180, 82)
Veronica = Person("Veronica", 168, 56)
Mateusz = Person("Matthew", 172, 70)



print(f" Veronica's BMI: {Veronica.bmi()}")
print(f" Jan's BMI: {Jan.bmi()}")
print(f" Matthew's BMI: {Mateusz.bmi()}")

# variables = atributes
# functions = methods