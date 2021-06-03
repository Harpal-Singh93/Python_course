class Employee:
    no_of_leaves=8

    # for  using constructor  we have to use def__init__() function

    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole



    # use of self

    def print_details(self):    # so self is used for taking object as a argument
        return f'Name is {self.name}, salary is {self.salary}, role is {self.role}'

#harry=Employee()
harry=Employee('Harry','45000','manager')
#harpal=Employee()

# harry.name='Harry'
# harry.salary=45000
# harry.role='manager'
#
# harpal.name='Harpal'
# harpal.salary=55000
# harpal.role='senior manager'
# print(harry.role)
#
# print(harry.print_details())  # in this case of object is harry and is passed



# use of constructor in python is done using
# def __init__()  using this function

print(harry.salary)   # this is printing the output using constructor
