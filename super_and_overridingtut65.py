class A:
    classvar1='I am a class variable in class A'
    def __init__(self):
        self.var1="i am inside class A's construtor"
        self.classvar1='instance variable in class A'
        self.special='special'   # we try to access this variable by running both constructor
        #at the same time using super()
class B(A):
    classvar1='I am in class B'  # attribute overriding
    def __init__(self):
        #super().__init__()  # this will first print a 's content than after below statement output got change to b
        self.var1="i am inside class B's construtor"
        self.classvar1='instance variable in class B'
       # super().__init__() # if we runn it here output will be in terms of a
        # if we comment above equation than output will be I am in class B
       # it will not go to class A instance because it is override by this class
       # constructor
        super().__init__()
        print(super().classvar1)


a=A()
b=B()
print(b.classvar1)
print(b.special,b.var1,b.classvar1)
#above condition will check for instance classvar1 first in class B and than it check in class
#  A if no instance variable found it will take a local one