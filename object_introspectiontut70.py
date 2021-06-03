"""Introspection is an ability to determine the type of an object at runtime.
Everything in python is an object. Every object in Python may have attributes and methods.
By using introspection, we can dynamically examine python objects. Code Introspection is used
for examining the classes, methods, objects, modules, keywords and get
information about them so that we can utilize it.
"""

class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        #self.email=f'{fname}.{lname}@codewithharry.com'
    def exlain(self):
        return f'This Employee is {self.fname} {self.lname}'
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return 'Email is not set.please set it using setter'
        return f'{self.fname}.{self.lname}@codewithharry.com'
    @email.setter
    def email(self,string):
        names=string.split('@')[0]
        self.fname=names.split(".")[0]
        self.lname=names.split('.')[1]

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None

skillf=Employee('Skill','F')
print(skillf.email)

#1:  type() : This function returns the type of an object.

print(type(skillf))
print(type('this is a string'))

#2. id() :This function returns a special id of an object.

print(id(skillf))
print(id('this is a string'))

#3. dir():This function return list of methods and attributes associated with that object.
o='harpal'
print(dir(o))
print(dir(skillf))
print(dir(Employee))

#4. inspect:  inspect.getmembers(object[, predicate])¶
"""
Return all the members of an object in a list of (name, value) pairs sorted by name. 
"""
import inspect
print(inspect.getmembers(skillf))