"""
Let's start the year learning "decorator pattern" in #python 🙌


This pattern allows a user to add new functionality to an existing object without altering its structure.
Creating a decorator class which wraps the original class and provides additional functionality keeping class methods signature intact.

When to use it?
- Want to augment an object with additional functionality.
- Do not want to rewrite or alter existing code.
- Want to keep new functionality separate.

Now, let's see it in action: 👀

1. Let's begin creating an interface.
An interface is used to specify the behavior of a class, we can achieve this with "abc" module.

2. Then create the component class that can be decorated.

3. Create the decorator class.
Decorator concept sample code


"""

from abc import ABCMeta, abstractmethod

class Icomponent(metaclass=ABCMeta):
    "Methods the component must implement"
    @staticmethod
    @abstractmethod
    def method():
        "A method to implement"
    
class component(Icomponent):
    "A component that can be decorated or not"
    def method(self):
        "An example method"
        return "Component Method"
    
class Decorator(Icomponent):
    "The Decorator also implements the IComponent"
    def __init__(self, obj):
        "Set a reference to the decorated object"
        self.object = obj
    def method(self):
        "A method to implement"
        return f"Decorator Method({self.object.method()})"
    
# The client
COMPONENT = component()
print(COMPONENT.method())
print(Decorator(COMPONENT).method())
