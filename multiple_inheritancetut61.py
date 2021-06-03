####   multiple inheritance   ######

class Employee:    # parent class1
    no_of_leaves=8
    var=5
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

class player:  #parent class2
    no_of_games=4
    var=6
    def __init__(self,name,game):
        self.name=name
        self.game=game
    def printdetails(self):
        return f'Name is {self.name}, game is {self.game}'

class coolprogrammer(Employee,player):
    language='c++'
#    var=7
    def print_language(self):
        print(self.language)

#employee class
harry=Employee('Harry','45000','manager')
harpal=Employee('Harpal','55000','senior manager')

#player class
shubam=player('shubam',['cricket'])

# coolprogrammer class
#karan=coolprogrammer()  this will give error as it try to run employee class
#constructor which has 3 arguments
karan=coolprogrammer('karan',40000,'coolprogrammer')
det=karan.print_details()
print(det)
karan.print_language()
print(karan.var)  # this will display 7 if same variable present in derived class
# if we comment var in coolprogrammer than it display 5
# as employee class is first in argument list

# note if we have a same variable name in classes than in which class code is
#running it will take its local variable .
#if both super classes has same variables than class which is first in the argument list
#whose variable will get display

# and if we change the order of arguments in class list in derived class
#than we need to match argument for that constructor
