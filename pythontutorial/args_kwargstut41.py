#  The special syntax *args in function definitions in python is used
#  to pass a variable number of arguments to a function.
#  It is used to pass a non-key worded, variable-length argument list.
# * operator always take input as tupple,list otherwise it make a tupple

# def funargs(*args):
#     print(type(args))
#     print(args[1])
#
# list=['hello','hi','namseste']
# funargs(*list)


# we can access all the element by using for loop

# def funargsname(*argsname):
#     for name in argsname:
#         print(name)
#
# list1=['harpal','aman','monu','pardeep','kamal']
# funargsname(*list1)

# we can also have normal argument as well as args well at the same time
# this order of argument must be kept 1.normal argument 2. args 3. kwargs

# def funargsname(normal,*argsname):
#     for name in argsname:
#         print(normal, name)
#
# list1=['harpal','aman','monu','pardeep','kamal']
# argu='hello'
# funargsname(argu,*list1)


# now we will use kwargs as well

def funargsname(normal,*argsname,**kwargs1):
    for name in argsname:
        print(normal, name)
    for key,value in kwargs1.items():
        print(f'{key} is a {value}')

list1=['harpal','aman','monu','pardeep','kamal']
argu='hello'
kw={'harpal':'teacher','aman':'MR','pardeep':'sofware engineer','kamal':'marketing officer'}
funargsname(argu,*list1,**kw)