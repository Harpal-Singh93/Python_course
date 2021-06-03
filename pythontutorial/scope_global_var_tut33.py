# x=20   # global variable
#
#
# def functinol(n):
#     #x=39 #local variable
#     y=20#local variable
#     global x      #use of global keyword to update the global variable
#     x=x+20
#     print(x)
#     print(n,'harpal')
#
#
#
# functinol('hello')
# print(x)
#print(y)  this will give error because y is a local variable of the function

#now we cannot update the global variable directly inside some other function
# we need to declare global inside that function than we can update it

##### use of global keyword inside a nested function

#case 1: when x is not declared outside

# def harpal():
#
#     x = 25
#
#     def rohan():
#         global x      #this will create a global variable x whose value is 88
#         x = 88
#     print('the value of x before calling rohan',x)
#     rohan()
#     print('the value of x after calling rohan',x)
#
# harpal()
# print(x)


#case 2: when x is declared outside

x = 50

def harpal():

    x = 25

    def rohan():
        global x       # in this case it will modify the global variable value from 50 to 88
        x = 88
    print('the value of x before calling rohan',x)
    rohan()
    print('the value of x after calling rohan',x)

harpal()
print(x)

