#syntax for list

myfirstlist=["hello",'hi',"namaste","sat shri akal","salam walekum"]
print(myfirstlist) #to access complete list

#to access particular element of the list
print(myfirstlist[4])

# similarly we can make a mix numbers and string list
mysecondlist=["hi","bye","forbade",45,56]
print(mysecondlist[2])


#some function of list
number=[2,34,5,6,7,10]
#number.sort()  # it will arrange the number in the list in increasing order
           #and this function will alter the original number list
#number.reverse()
# similarly we can do slicing as done in previous tut
#note nerver take any number less than -1 in extended slicing [::-2 or -3 etc] it will work in this case
#but in first 2 colon if there are any value than it will not work properly

print(min(number))
print(max(number))
print(len(number))
number.append(45)  # it will add number to the end of the list
number.append(45)  # so in list if we add same element twice it will taken two times
number.append(66)
print(number)
number2=[]  #sometime we make a empty string and than add the elements later on
number2.append(23)
number2.append(34)
print(number2)

#if we want to add element in between of the list than we can use insert function

number.insert(1,33)  #where 1 is index and 33 is value to be added
#similarly we can remove any element
number.remove(45)

#to remove 1 element from the last we can use pop function
number.pop()
print(number)


#in list we can modify any element but in case of tupple we cannot modify
#the elements of the tupple
#mutable= which can change -> list
#immutable=which cannot change->tupple

t1=(1,2,3,45,6)
print(t1)
#we cannot perform modification in tupple as shown below
# t1[2]=8  it will give error
# we have one element in tupple than we have to mention a comma after it otherwise it will not consider it as tupple
t2=(2)
print(t2)
t3=(2,)
print(t3)

# to swap two numbers
a=4
b=5
"""   
traditional ways of swapping two numbers
temp=a
a=b
b=temp
"""
a,b=b,a   # this we how swap in python
print(a,b)