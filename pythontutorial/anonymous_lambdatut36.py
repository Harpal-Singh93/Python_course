# anonymous and lambda function is a one liner function like

# def minus(a,b):
#     return a-b

# above and below functions are doing the same job

minus=lambda a,b:a-b

print(minus(7,5))
 # another example
# traditional approach
def a_first(a):
    return a[1]

list=[[1,5],[3,15],[5,2],[7,8]]
list.sort(key=a_first)
print(list)

#with the use of lambda function

list=[[1,5],[3,15],[5,2],[7,8]]
list.sort(key=lambda x: x[1])
print(list)


