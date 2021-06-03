mystr="suresh is a Very good boy"
print(mystr)

print(mystr[2])
print(mystr[0:3])  # it will show characters from 0 to 2 it will show one element less than right side

#to check the length of string

print(len(mystr))

#some cases
# print(mystr[78])  this line will give error
print(mystr[0:78])  #this line will not give error

print(mystr[0:5:2]) #this statement will take o to 4 elements and it will take the gap of 1 element
print(mystr[:5]) # it will start from 0 to 4
print(mystr[0:]) # it will print till end
print(mystr[:]) #it will also print till end
print(mystr[::]) #it will also take it complete
print(mystr[0:25:1])# these are default values taken by compiler in above case

print(mystr[0::3]) #it will skip 2 elements
print(mystr[0::9]) # it will skip 8 elements

print(mystr[::7864]) #it  will try to resolve until it can


#negative indices

print(mystr[-5:-1])
print(mystr[20:24]) # so above and this statement do identical work
print(mystr[::-1])  # it will reverse the string
print(mystr[::-2])  #it will first reverse the string and than skip one elements


#some other functions

print(mystr.isalnum()) # this string functions  Returns True if all characters in the
# string are alphanumeric

print(mystr.isalpha())  # Returns True if all characters in the string are in the alphabet

print(mystr.endswith("oy"))
print(mystr.endswith("girl"))  #these statement helps to check how the line ends


# to count the number of times a special character exist or not
print(mystr.count("o"))

#to capitialize the initial character of string
print(mystr.capitalize())

# to find about any special world starting  character position
print(mystr.find("good"))  #so g of good is at 17 poistion of the string


#to lower all letters
print(mystr.lower())

#to upper all letters
print(mystr.upper())

#to replace any word with the another
print(mystr.replace("is","are"))