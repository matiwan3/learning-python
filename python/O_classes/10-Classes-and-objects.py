class MyClass:
    varaible = "blah"
    
    def my_function(self):
        print("This is a message inside the class.")
        
myobjectx = MyClass()

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.varaible = "yackity"

# Then print out both values
print(myobjectx.varaible)
print(myobjecty.varaible)