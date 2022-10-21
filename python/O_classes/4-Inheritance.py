'''
https://docs.python.org/3/tutorial/classes.html
'''
# inheritance = dziedziczenie (w programowaniu obiektowym) //diki
# Of course, a language feature would not be worthy of the name “class” without supporting inheritance. 
# The syntax for a derived class definition looks like this:
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
    # The name BaseClassName must be defined in a scope containing the derived class definition. 
    # In place of a base class name, other arbitrary expressions are also allowed. This can be useful,
    # for example, when the base class is defined in another module:
    
class DerivedClassName(modname.BaseClassName):
    
    
### Multiple Inheritance ###

class DerivedClassName(Base1, Base2, Base3):
    