#file opening basics
#without any mode mentioned so by default it is open in text and in reading mode

# f=open("new file.txt")
# content=f.read()
# print(content)
# f.close()

# let's open in some modes
# f=open("new file.txt",'r+b')   #reading in binary mode
# print(f.read())
# f.close()

# f=open("new file.txt",'a')   #using appending mode
# print(f.write('\nhello'))
# f.close()

# use of read function

# f=open("new file.txt")
# content=f.read(3)       # it will read 3 letters
# print(content)
#
#
# content=f.read(3)
# print(content)         #it will read next 3 letters
# f.close()

# if we use bigger number in read function

# f=open("new file.txt")
# content=f.read(3445)       # it will read all letters
# print(content)
#
#
# content=f.read(3345)
# print("2",content)         #this become useless as already all the data has been read
# f.close()


# we want to print line by line
#
# f=open("new file.txt")
# #content=f.read()
#
# # for line in content:       it will print character by character
# #     print(line)
#
# for line in f:
#     print(line,end='')     #it will print line by line complete lines


### for printing one line at a time

# f=open("new file.txt")
# print(f.readline())
#
# print(f.readline())
# f.close()
### for reading multiple lines we can use readlines

# f=open("new file.txt")
# print(f.readlines())
# f.close()