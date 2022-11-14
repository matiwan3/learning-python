# Class Method
# classmethod()

class TestClass:
    def regular_method(self):
        print(self)
        
    @classmethod
    def class_method(cls):
        print(cls)
        
    def __str__(self):
        return "TestClass Instance"
    
t = TestClass()
t.regular_method()
t.class_method()
TestClass.class_method()
    