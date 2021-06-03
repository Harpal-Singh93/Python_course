#function definition
def even_odd(z):
    """program for finding whether a number is even or odd"""     #this is docstring
    if z%2==0:
        print(z," is even")
    else:
        print(z,'is odd')


#driver code
print(even_odd.__doc__)    #syntax for calling docstring
even_odd(2)    #function call with single parameter
even_odd(3)

#use of return statement with the help of another function for finding sqaure of a number

def square_num(x):
    return x**2

q=square_num(3)
print(q)


#note in python it is always pass by reference case for example
def func1(x):
    x[0]=1

lst=[10,20,30,40,50]
print(lst)   #before passing
func1(lst)
print(lst)   #after passing through the function

#but above is not the case if we change the entire list
def func2(y):
    y=[1,2,3]

lst1=[10,20,30,40,50]
print(lst1)   #before passing  in this case link of y with previous object get broken
func2(lst1)   #and a new object is assigned to y
print(lst1)


#default argument

def my_fun(x,y=34):
    print("x is ",x)
    print("y is ", y)


my_fun(10)
my_fun(10,20)

#keyword Argument

def student(first,last):
    print(first,last)

student(last='singh',first='harpal')
student(first='singh',last='harpal')

#variable length or arbitrary argument

def greet(*name):
    for val in name:
     print("hello ",val)

greet('harpal','raman','nitish')

#anonymous function or lambda function

sum=lambda arg1,arg2:arg1+arg2    #this is way these functions are defined

print("the sum is ",sum(1,4))




