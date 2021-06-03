# # basic for writing in a file
# w mode
# f=open("file_writing.txt",'w')
# f.write('hello this is my first time writing in a file in python')
# f.close()

# append (a) mode
#
# f=open("file_writing.txt",'a')
# f.write('\nhello buddy')
# f.close()

# to get the length of data in file we can use this write method

# f=open("file_writing.txt",'a')   # we can also use here write mode
# a=f.write('\nhello buddy')
# print(a)
# f.close()

# to read and write at the same time 'r+' mode

# f=open("file_writing.txt",'r+')   # we can also use here write mode
# print(f.read())
# f.write('hello buddy')
# f.close()