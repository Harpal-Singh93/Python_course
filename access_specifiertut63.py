#public----> any one can access it
# use the variable as it is public by default

#protected----> derived classes can access it
# we use single underscore in front of variable name to declare it as protected variable

#private----> no one can access it without permission
# we use double underscore in front of variable name to declare it as private variable
#in python private variables can be accessed using special syntax that is known as name mangling

# using same code from tut58
#####   single level inheritance   ######

class Employee:
    no_of_leaves=8   # this is a public variable
    _protect=45      # this is a protected variable
    __private=34     # this is a private variable
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def print_details(self):
        return f'Name is {self.name}, salary is {self.salary}, role is {self.role}'

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    @classmethod
    def from_dash(cls,string):

          return cls(*string.split('-'))

    @staticmethod
    def print_good(string):
        print('this is good'+string)

# child class or derived class
class programmer(Employee):
    no_of_holidays=28
    def __init__(self,aname,asalary,arole,languages):
       self.name=aname
       self.salary=asalary
       self.role=arole
       self.laguages=languages

    # self method for programmer class
    def print_prog(self):
        return f'The programmer name is {self.name}. Salary is {self.salary} and role is {self.role}.' \
               f'The lagnuages are {self.laguages}'


harry=Employee('Harry','45000','manager')
harpal=Employee('Harpal','55000','senior manager')

aman=programmer('Aman','40000','MR','English')
print(aman. _protect)   # so derived programmer class can access a protected variable

#print(aman.__private)  # this will give a error as we cannot directly access a private variable

#to access private variable we have to use name mangling
print(aman._Employee__private)    # this is how we can access a private variable
