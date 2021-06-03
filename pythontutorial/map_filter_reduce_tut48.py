# concept of map
# in the scenrio given below we are using a for loop and typecasting
#tool to get add a string to a number. instead of that we can use map function
numbers=['3','56','34']

# for i in range(len(numbers)):
#     numbers[i]=int(numbers[i])
numbers=list(map(int,numbers))  # this single does functioning of above 2 lines

numbers[2]=numbers[2]+4
print(numbers[2])

# another example of a map

def sq(a):
    return a*a
lis=[1,2,3,4,5]
square=list(map(sq,lis))   # working of map function to find a square of number
print(square)

#we can also use lambda function inside a map

lis1=[6,7,8,9,10]
square1=list(map(lambda x:x*x,lis1))
print(square1)

#another example of lambda with map

def square2(a):
    return a*a
def cube(a):
    return a*a*a
func=[square2,cube]

for i in range(5):
    val=list(map(lambda x:x(i),func))
    print(val)

###### use of filter function #########

list_2=[1,2,3,4,5,6,7,8,9]

def is_greater_5(num):
    return num>5

gr_than_5=list(filter(is_greater_5,list_2))
print(gr_than_5)

###### use of reduce #######

#suppose if we want to add all the elements of the list
#we can use for loop
# else we can use reduce method

# list3=[1,2,3,4,5]
# num=0
# for i in list3:                      instead of using this code we will prefer reduce method
#     num=num+i
# print(num)
from functools import reduce
list3=[1,2,3,4,5]
num=reduce(lambda x,y:x+y,list3)      # so this lines do the functioning of above three lines
print(num)

