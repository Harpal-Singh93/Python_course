s=set()
print(type(s))
s_from_list=set([1,2,3,4,5,6])
print(s_from_list)
print(type(s_from_list))

# to add element in the set
s.add(1)
s.add(1) # this is main difference between set and other data type it will take only unique values as input4
s.add(2)
s1=s.union({1,2,3,4}) #union of two s with {1,2,3,4] set
s2=s.intersection({2,3})
print(s)
print(s1)
print(s2)
print(s.isdisjoint(s2)) # to check set are disjoint or not
#similarly we have other functions like min,max,len etc.

print(s.remove(2))
print(s)