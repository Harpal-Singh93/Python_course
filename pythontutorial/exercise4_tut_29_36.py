# this is exercise in this case if true input is coming we are printing straight star pattern
#if false or zero input case we are printing reverse pattern

print('enter the number of rows for star pattern')
n=int(input())

print('enter either 0 for reverse star pattern  or 1 for straight star pattern')
z=int(input())
new=bool(z)

if new==True:
    for i in range(0,n):
        for j in range(i+1):
           print('*',end='')
        print()
elif new==False:
    for i in range(n,0,-1):
        for j in range(i):
           print('*',end='')
        print()



