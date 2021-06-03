# import sklearn as sk
# print(sk.__version__)

# import sys
# print(sys.path)   # it will print the order where it look for the module
# you want to use like it will search sklearn in first path and than second path and so on...
#until it find out so never give a file name same as module name


# we can also import our own module or any other file
#we can use its function and variables

# import file1
# print(file1.a)    # this is good practice

# we can also use this way
# from file1 import a    # but this method is not advisable
# print(a)

import file1
file1.printjoke('hello how are you')
