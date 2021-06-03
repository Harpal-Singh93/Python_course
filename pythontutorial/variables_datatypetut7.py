#Different types of variables & printing them
var1="hello world"
var2=45
var3=4.6
var4=" welcome me"
print(var1)
print(var2)
print(var3)

# to check the data type of the variable
print(type(var1))
print(type(var2))
print(type(var3))

#to when we use  addition operator between numbers and strings
print(var3+var2)
#print(var2+var4)  this will give error because we cannot add number and string
print(var1+var4)
var5="50"
var6="70"
print(var5+var6)

# to typecaste any data type into another
"""
we can use 
int()
float()
str()    to typecaste one type of variable into another
"""
print(int(var5)+int(var6))
print(float(var2))

#extra

print(5*"hello world\n") # this will print hello world 5 times
print(100*str(int(var5)+int(var6)))

# for taking input from the user
print('enter a number')
inpnum=input()   #input function take input from the user and it return a string always
print("entered number is ",inpnum)
#print("entered number is ",inpnum+10) this line will give error because we cannot add number with string
print("entered number and sum is ",inpnum,int(inpnum)+10)


#quiz
print("enter first number")
var7=int(input())
print("enter second number")
var8=int(input())
print("the sum is ",var7+var8)