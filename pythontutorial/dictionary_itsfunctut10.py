#dictionary is nothing but key value pair

d1={}
t1=()
li=[]
print(type(d1))
print(type(t1))
print(type(li))


# dictionary starts from here

d2={"harpal":"masala dosa","satbir":"chicken",
    "bholi":"chole bathore"}
print(d2)
print(d2["harpal"])
# we can make elements of dictionary as  further dictionary as shown below
d3={"harpal":"masala dosa","satbir":"chicken",
    "bholi":"chole bathore","kamal":{"breakfast":"chicken","lunch":"fish","dinner":"egg"}}
print(d3["kamal"])
print(d3["kamal"]["lunch"])


# we want to add element later on in the dictionary

d2["harry"]="samose chole"
print(d2)
d2[34]="kuch nai khana"
print(d2)

#to delete a element from dictionary
del d2[34]
del d2
print(d2)

# use of copy in case of dictionary

#d4=d2 # by this equation it will not create a separate copy of d2 and store in d4
#in this case they both are pointers which are pointing to the same locations
#so changes made in d4 will refelect in d2 as well
#del d4[ "harry"]
#print(d2)
# so to avoid above issue we use copy function
d4=d2.copy()
del d4["harry"]
print(d2)

#other functions

print(d2.get("harry"))  # it will get the value of harry

d2.update({"lenna":"kulche chole"}) # to add another element in dictionary

print(d2)

print(d2.keys())  # to get all the key point
print(d2.values())  # to get all the values 
