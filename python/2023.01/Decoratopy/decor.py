"""
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