# using same code from tut56

class Employee:
    no_of_leaves=8



    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def print_details(self):
        return f'Name is {self.name}, salary is {self.salary}, role is {self.role}'

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    @classmethod        #this will work as alternative constructor
    def from_dash(cls,string):
        # params=string.split('-')
        # print(params)                      #in stead of writing these 3 lines we can use
        # return cls(params[0],params[1],params[2])    # args here this will pack all variables
          return cls(*string.split('-'))

harry=Employee('Harry','45000','manager')
harpal=Employee('Harpal','55000','senior manager')
sunil=Employee.from_dash('Sunil-50000-engineer')     # we are using class method to work as alternative constructor
print(sunil.salary)
print(sunil.name)
# harpal.change_leaves(34)
# print(harry.no_of_leaves)
# Employee.change_leaves(27)
# print(Employee.no_of_leaves)




# print(harry.salary)
