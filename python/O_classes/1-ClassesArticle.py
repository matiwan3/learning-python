# Python Class Methods: Class Vs. Instance Vs. Static Methods

# In this article we are going to look at methods that we can use in Python classes. 
# Methods are essentially functions within a class. 
# In Python, we can use three (3) different methods in our classes: 
# class methods, 
# instance methods, 
# and static methods. 
# We are going to look at how each method differs from the other. 
# Before we dive into the methods, let's look at two types of attributes that we find in classes. 
# Understanding class attributes is crucial to understanding methods.

# Class Attributes
# What is a class attribute? A class attribute is a variable that belongs to a class. 
# It is a property of the class. It belongs to the class rather than any specific object. ``
# This attribute is created outside of the constructor method (__init__). 
# Below, we have a code that demonstrates how we create class attributes in a class.

class Animals:
    # Class atribute
    home = 'zoo'
    
# Instance Attributes

# Class attributes (variables) belong to a class and not to a specific object. 
# However, we can also create instances that belong to an object or instance. 
# These attributes are called "instance attributes." Instance attributes are created inside a constructor. 
# The constructor for instance attributes is the __init__() method. 
# The constructor initializes the instance attributes. The first parameter of the constructor is self. 
# The attributes of the instance come after the "self" parameter. 
# See the code below.

    #creating instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
# Class Methods

 ##################### class attributes and instance attributes. #####################
# Class methods are methods that are not bound to an instance of a class (object) but to the class itself. 
# Remember, there are two types of attributes in a class; class attributes and instance attributes. 
# Class attributes are bound to the class, while instance attributes are bound to an object. 
# Class methods can only access and modify class attributes and not instance attributes. 
# There are two ways to create a class method. The first method is to use the classmethod() function. 
# The second method is to use the @classmethod decorator. In this article, we are going to use the decorator to create a class method. 
# The first parameter of this class method is "cls". The "cls" keyword simply means "referring to the class." 

# In our class below, there is a class attribute called "home." 
# We create a class method that can access and modify this class attribute. 
# We create a function called "animals_home." Right at the top of the function, we add the decorator @classmethod. 
# This decorator converts the function into a class method. We use this method to change the class attribute. 
# We change the home variable, from "Zoo" to "Jungle". This proves that class methods can access and change class attributes.
    @classmethod
    def animals_home(cls, home):
        cls.home = home
    
    # creating instance method
    
    
#creating Animals instances
# animal1 = Animals("Lion", 4)
# print(f'The Original animals home is a {animal1.home}')

# #changing class attributes using class method
# Animals.animals_home("Jungle")
# print(f'The new animals home is the {animal1.home}')

# Instance Methods

# Now let's look at instance methods. Instance methods can access and modify both class attributes and instance attributes. 
# Similar to a class method, an instance method is just a function in a class. It also starts with the keyword "def". 
# Its first parameter is the keyword "self". The self parameter binds the method to the instance object. 
# In the code below, we have added an instance method called insta_method. 
# Notice that this insta_method has access to the attributes of the object (name and age) and the class attributes (home). 
# Notice that we have changed the class attribute (home) value from "zoo" to "jungle". 
# When we call the instance method using the animal1 (animal1.insta_method) object, 
# you can see that the output for location says "jungle" instead of "zoo". 
# Instance methods are used more often than class methods because they can access both class and instance attributes.

    def insta_method (self):
        #modyfying the class attribute
        self.home = "jungle"
        return f'Name: {self.name}, Age: {self.age}, ' \
            f'Location: {self.home}'
            

# Static Methods

# Unlike instance and class methods, static methods cannot access class attributes or instance attributes. 
# In Python, we create a static method using a decorator. We write @staticmethod right above the method we want to decorate. 
# Static methods have no implicit first argument. Neither cls nor self is passed as the first argument. 
# Static methods are just functions that you can call from the class or instance of the class. 
# Below, we have added a static method to our code. 
# This method takes one argument, which is the age of the animal, and checks if the animal is an adult or not. 
# Notice that we are using the animal instance (animal1) to call the static method. Static methods are simply utility or helper functions. 
# They add extra functionality to a class without accessing or modifying the class state.

    @staticmethod
    def check_age(age):
        if age > 5:
            return 'Adult'
        else:
            return 'Not adult'

# creating Animals instances
animal1 = Animals("Lion", 4)
print(animal1.insta_method())
# calling static method using class instance
print(animal1.check_age(4))

# Summary

# Class methods can access class attributes, but they cannot access instance attributes. 
# Instance methods can access both class and instance attributes. Static methods are just utility functions. 
# They do not have access to class attributes or instance attributes.


        
        
        
        
        
        