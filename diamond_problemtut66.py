"""
Diamond problem
It refers to an ambiguity that arises when two classes Class2 and Class3 inherit
from a superclass Class1 and class Class4 inherits from both Class2 and Class3.
If there is a method “m” which is an overridden method in one of Class2 and Class3
or both then the ambiguity arises which of the method “m” Class4 should inherit.
"""
#case 1:when method is written in one class

# class A():
#     def m(self):
#         print('This is a method from class A')
# class B(A):
#     pass
# class C(A):
#     pass
# class D(B,C):
#     pass
# obj =D()
# obj.m()

#case 2:when method is overriden in two class

# class A():
#     def m(self):
#         print('This is a method from class A')
# class B(A):
#     def m(self):
#         print('This is a method from class B')
# class C(A):
#     pass
# class D(B,C):
#     pass
# obj =D()
# obj.m()

#case 3:when method is overriden in three class

# class A():
#     def m(self):
#         print('This is a method from class A')
# class B(A):
#     def m(self):
#         print('This is a method from class B')
# class C(A):
#     def m(self):
#         print('This is a method from class C')
# class D(B,C):   # we we change the order of parameter than output will be in terms of C
#     pass
# obj =D()
# obj.m()


#case 4:when method is overriden in all class

class A():
    def m(self):
        print('This is a method from class A')
class B(A):
    def m(self):
        print('This is a method from class B')
class C(A):
    def m(self):
        print('This is a method from class C')
class D(B,C):
    def m(self):
        print('This is a method from class D')
obj =D()
obj.m()