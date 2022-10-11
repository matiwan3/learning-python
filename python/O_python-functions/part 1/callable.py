# Callable
# callable()
# useful to know when can i call something 
class Class:
    pass

def func():
    print("hi")
    
def func2():
    def inner():
        pass
    
    return inner

func3 = lambda x: x + 1 #anonymous function
not_func = "hello"

print(callable(Class))
print(callable(func))
print(callable(func2()))
print(callable(func3))
print(callable(not_func))