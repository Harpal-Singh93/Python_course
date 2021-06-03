"""
A class is called an Abstract class if it contains one or more abstract methods.
An abstract method is a method that is declared, but contains no implementation.
Abstract classes may not be instantiated, and its abstract methods must be implemented by its subclasses.
"""

#from abc import ABCMeta,abstractmethod  # this syntax is for python version 3.4 or below
from abc import ABC,abstractmethod
class Shape(ABC):  # we are using first import statement than  parameters needs to be metaclass=ABCMeta
    @abstractmethod
    def print_area(self):
        return 0

class Rectangle(Shape):
    type='Rectangle'
    side=4
    def __init__(self):
        self.length=6
        self.breadth=7

    def print_area(self):
        return self.length * self.breadth

rt=Rectangle()   # this will give error if print_area function is not present in class rectangle
print(rt.print_area())

#obj=Shape()  it will give error
#note we cannot create object of base abstract class