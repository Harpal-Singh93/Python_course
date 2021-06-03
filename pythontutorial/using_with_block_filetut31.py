# we can use 'with' block open and close a file

with open('new file.txt') as f:
    a=f.read(10)
    print(a)


#quiz of the day can we use now the simple the previous method same time now

z=open('new file.txt')
a=z.read()
print(a)
z.close()

# answer yes we can do so