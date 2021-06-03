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

    @classmethod
    def from_dash(cls,string):

          return cls(*string.split('-'))

    # static method : in which we don't want to use either class argument or self argument then we use
    #static method. we declare it inside a class
    @staticmethod
    def print_good(string):
        print('this is good'+string)  # output will show none because we didnot return anything


harry=Employee('Harry','45000','manager')
harpal=Employee('Harpal','55000','senior manager')
sunil=Employee.from_dash('Sunil-50000-engineer')
# print(sunil.salary)
# print(sunil.name)
# harpal.change_leaves(34)
# print(harry.no_of_leaves)
# Employee.change_leaves(27)
# print(Employee.no_of_leaves)
print(harry.print_good('Harry'))  # it will display none also as function doesnot return anything
harpal.print_good(' Harpal')
# we can also use class here
Employee.print_good(' Singh')



# print(harry.salary)
