# Python Classes and Objects
'''
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.
'''

# Create a Class

class people:
    name = ""
    number = ""

person = people();
person.name = "Mahin Jaman";
person.number = 1711112222;
print(person.name);
print(person.number);