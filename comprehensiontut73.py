"""Comprehensions in Python provide us with a short and concise way
 to construct new sequences (such as lists, set, dictionary etc.)
 using sequences which have been already defined. Python supports the following 4 types of comprehensions:

1.List Comprehensions 2.Dictionary Comprehensions 3.Set Comprehensions 4.Generator Comprehensions
"""
# 1. list comprehension

# traditional approach
# ls=[]
# for i in range(100):
#     if(i%3)==0:
#         ls.append(i)
# print(ls)

# with comprehension
ls=[i for i in range(100) if i%3==0]
print(ls)


# 2.Dictionary Comprehensions

# dict1={i:f"item{i}" for i in range(1,10001) if i%100==0}
dict1={i:f"item{i}" for i in range(5)}
# we can also reverse the order of dictionary elements value,key from key,value pair
dict2={value:key for key,value in dict1.items()}

print(dict1,'\n',dict2)


# 3.Set Comprehensions

dresses={dress for dress in ['dress1','dress2','dress3','dress1','dress2']}
print(dresses)
print(type(dresses))

#4.Generator Comprehensions

evens=(i for i in range(100) if i%2==0)
print(evens.__next__())
print(evens.__next__())

  ## or we can use for loop for printing all the value of generator object

for i in evens:
    print(i)