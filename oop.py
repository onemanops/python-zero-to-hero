# Object-oriented programming: 
# 
# Object-oriented programming (OOP) is a programming paradigm that allows you 
# to model real-world concepts using classes and objects. In Python, you can 
# define classes using the class keyword, and you can define methods and 
# attributes using the self keyword. 


class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print("Woof!")

dog1 = Dog("Fido", "Labrador", 3)
dog2 = Dog("Buddy", "Poodle", 5)

print(dog1.name)  # prints "Fido"
print(dog2.breed)  # prints "Poodle"

dog1.bark()  # prints "Woof!"
dog2.bark()  # prints "Woof!"

# In this example, we define a Dog class with a __init__ method that is called 
# when a new Dog object is created. The __init__ method sets the name and age 
# attributes of the object. We also define a bark method that prints "Woof!" 
# when called.

# We then create two Dog objects, dog1 and dog2, and set their name, breed and age 
# attributes. We can access these attributes using the dot notation (e.g. 
# dog1.name). We can also call the bark method on these objects (e.g. dog1.bark()).