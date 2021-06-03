####### some concepts from functions

# 1. if we assign a function to another function and deleting the previous
#one than the new function will work absoultely fine.

def function1():
    print('hello')

function2=function1
del function1
function2()

# 2. we can return a function from a function

def funcret(num):
    if num==1:
        return print
    if num==2:
        return sum

a=funcret(1)
print(a)

#3. we can pass function as a argument of another function

def executer(func):
    func('this is pycharm software')

executer(print)

################ Decorators ############

def dec1(func1):
    def nowexec():
        print('executing now')
        func1()
        print('executed')
    return nowexec
@dec1
def who_is_mohit():
    print('mohit is a doctor')

#who_is_mohit=dec1(who_is_mohit)    # this line is decorator we are changing the functionality of who is mohit function
who_is_mohit()

# another symbol of decorator is @fucntion_name
# so we have two choices either write  who_is_mohit=dec1(who_is_mohit) this line
#or write @dec1 before the definition of who_is_mohit() function
