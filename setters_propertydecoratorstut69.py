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

harpal=Employee('Harpal','Singh')

#print(harpal.exlain())
# print(harpal.email) # first we use email as instance variable
# as we made them function now so
#print(harpal.email())   # we want to avoid function call() brackets we need to use property decorator
print(harpal.email)


# if we want to change the name of Harpal to Kamal
harpal.fname="kamal"  # this will not get change directly if it is a instance variable
# we can change it by creating a same name function
#print(harpal.email)
#print(harpal.email())
print(harpal.email)

# now if we want to change email function value

harpal.email='this.that@codewithharry.com'
print(harpal.email)  # this will not work directly so we need setter to do this thing


# now if we want to delete that email
del harpal.email  # we cannot do this directly as we need to create a deleter
print(harpal.email)   # it will print now None.None@codewithharry.com
# to avoid this none.none we will use a if condition