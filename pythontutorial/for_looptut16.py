#use of for loop in list
list1=['harpal','aman','monu','pardeep']  #we can also iterate a tuple,list
for items in list1: # here items is a variable any name can be used here
    print(items)
#use of for loop in case of list of list
list2=[['harpal',1],['aman',2],['monu',3],['pardeep',4]]
for items1 in list2:
    print(items1)

#similarly we can unpack a list of list using another variable in for loop
list2=[['harpal',1],['aman',2],['monu',3],['pardeep',4]]
for items1,lollypop in list2:
    print(items1,"eats lollypop are ",lollypop)

#we can use it in case of dictionary as well
dict1=dict(list2) #typecasting list into a dictionary
#print(dict1)
for items,lollypop in dict1.items():
    print(items,lollypop)

    # for printing only keys
    for items in dict1:
        print(items)

        #use of for loop in case of if statement do your own:

       # quiz: print only character which is number and greater than 6 same in a mixed list

list3=['harpal',1,2,6,7,8,'bye']
for item in list3:
    if str(item).isnumeric() and item>6:
        print(item)

