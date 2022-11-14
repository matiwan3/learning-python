# class MyClass:
#     variable = "blah"
    
#     def function(self):
#         print("This is a message isnide the class.")
        
# myobjectx = MyClass()

# myobjectx.function()

# Init()

class NumberHolder:
    
    def __init__(self, number):
        self.number = number
        
    def returnNumber(self):
        return self.number

var = NumberHolder(7)
print(var.returnNumber())