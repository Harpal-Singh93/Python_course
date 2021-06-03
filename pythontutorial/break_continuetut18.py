i=0
while(1) :
    if i+1<5:
        i=i+1
        continue
    print(i+1, end=" ")
    i = i + 1
    if(i==44):
        break

#quiz take input from the user until input entered by user is less than 100

while(1):
    print("enter any number")
    a=int(input())
    if a>=100:
        print("thanks you win")
        break
    else:
        print("try again")
        continue
