# in this tutorial we are changing value of a class variable
# using a class method so that values can be updated using class
# as well as its instance

class Employee:
    no_of_leaves=8



    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def print_details(self):
        return f'Name is {self.name}, salary is {self.salary}, role is {self.role}'

    @classmethod      # this is used for creating a class method so that we can update class varaible
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves


harry=Employee('Harry','45000','manager')
harpal=Employee('Harpal','55000','senior manager')

harpal.change_leaves(34)
print(harry.no_of_leaves)
Employee.change_leaves(27)
print(Employee.no_of_leaves)




print(harry.salary)   # this is printing the output using constructor
