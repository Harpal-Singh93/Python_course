# using same code from tut58
#####   single level inheritance   ######

class Employee:    # parent class or super class
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

    @staticmethod
    def print_good(string):
        print('this is good'+string)

# child class or derived class
class programmer(Employee):
    no_of_holidays=28
    #constructor for programmer class
    #note the we don't need to create a constrcutor for derived class
    # we have to use 'super' method. but write now we using like previous one only

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
sunil=Employee.from_dash('Sunil-50000-engineer')

aman=programmer('Amandeep','60000','MR',['English'])
pardeep=programmer('Pardeep','80000','software engineer',['python'])

print(pardeep.print_prog())    # same class method got executed
print(pardeep.print_details())  # it can access the super class method
print(pardeep.no_of_holidays)

