# # factorial of a number using iterative approach
# ### as we know for calculating factorial of a number we use the formula
# ### n!=n*(n-1)*(n-2)....3*2*1
# ### n!=n*(n-1)!
# ### 0!=1
#
# # so this is iterative approach for calculating factorial
#
# def iterative_fun(n):
#     if n==0:
#         return 1
#     else:
#         fac=1
#         for i in range(n):
#            fac=fac*(i+1)
#     return fac
#
# # this is recurisve approach
#
# def recursive_fun(n):
#     if (n==0) or (n==1):
#         return 1
#     else:
#         return n*recursive_fun(n-1)
#
# # inside working of recursive function like this example of 4!
# # 4*recursive_fun(3)
# # 4*3*recursive_fun(2)
# # 4*3*2*recursive_fun(1)
# # 4*3*2*1=24
#
# print('enter a number whose factorial you want')
# num=int(input())
# print(iterative_fun(num))
# print(recursive_fun(num))



#program for a fibonacci series 0,1,1,2,3,5,8,13,21,34,55 so on

def fibo_fun(num):
    if (num==1):
        return 0
    elif (num==2):
        return 1
    else:

        return fibo_fun(num-1)+fibo_fun(num-2)


print('enter the position which fibonacci number you want ')
num2=int(input())
print(fibo_fun(num2))