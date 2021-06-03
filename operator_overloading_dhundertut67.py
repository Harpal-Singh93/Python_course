"""
Dunder or magic methods in Python are the methods having two prefix
and suffix underscores in the method name. Dunder here means “Double Under (Underscores)”.
These are commonly used for operator overloading. Few examples for magic
methods are: __init__, __add__, __len__, __repr__ etc.
"""

class Employee():
    no_of_leaves=8

    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f" The name is {self.name}, Salary is {self.salary} and Role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    # overloading '+' operator  below
    def __add__(self, other):     # so we have overload the + operator here with the help of dunder
        return self.salary + other.salary    # method __add__

    # overloading '/'operator  below
    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
       # return self.printdetails() # output in this case :The name is Harpal, Salary is 45000 and Role is Programmer
         return f'Employee({self.name},{self.salary},{self.role})' # this is how repr method is used generally
    def __str__(self):
        return f" The name is {self.name}, Salary is {self.salary} and Role is {self.role}"

emp1=Employee('Harpal',45000,'Programmer')
emp2=Employee('Rohan',50000,'Sr. Manager')
#print(emp1+emp2)  # as we cannot directly add two objects with each other directly
# we have to use dunder methods for it.
#print(emp1/emp2)

print(emp1)
#print(repr(emp1))
# if we directly print an object it will display its address
# but if we use __repr__ and str method than the output is different
#note. if both str and repr is present by default str will work
#we have to call spearately print(repr(emp1)) to print using repr in this case

############ for more dunder function check for Mapping operator to functions in google#############