class Employee:
    no_of_leaves=8   # this is class variable and any instance can access this variable
    # but to change this variable no instance can change it can be change only by Employee class only
    pass

harry=Employee()
harpal=Employee()

harry.name='Harry'    # harry is a instance of class employee
harry.salary=45000    # name,salary,role are its own variables of harry
harry.role='manager'  # these variable has nothing to do with the class

harpal.name='Harpal'    # harpal is a instance of class employee
harpal.salary=55000    # name,salary,role are its own variables of harpal
harpal.role='senior manager'  # these variable has nothing to do with the class

print(harpal.role)
print(harry.no_of_leaves)
print(harpal.no_of_leaves)
print(Employee.no_of_leaves)
harpal.no_of_leaves=10   # this will not change the value of no_of_leaves variable in class
# its create a local variable for harpal object we can verify it using __dict__
print(harpal.__dict__)     # no of leaves 10 here
print(Employee.__dict__)   # no. of leaves 8 here
# to change the no_of leaves inside class we have to use below code
Employee.no_of_leaves=11
print(harry.no_of_leaves)   # now the value got changed for every other object also
