class Car:
    color = "white"
    
    def __init__(self, mark):
        self.mark = mark
        
carl = Car("Ford")
print(Car.mark) # attributeError because class Car has no attribute "make"