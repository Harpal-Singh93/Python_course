def getdate():
    import datetime
    return datetime.datetime.now()

def take(z):
    if(z==1):
        print('press 1 for food log and press 2 for exercise log')
        c=int(input())
        if(c==1):
            print('enter the food eat')
            value=input()
            with open('harry_food.txt','a') as op:
                op.write(str([(str(getdate()))])+':'+value+'\n')
            print('sucessfully written')
        elif(c==2):
            print('enter the exercise')
            value = input()
            with open('harry_exerc.txt', 'a') as op:
                op.write(str([(str(getdate()))]) + ':' + value + '\n')
            print('sucessfully written')
        else:
            print('wrong option selected')
    elif (z == 2):
        print('press 1 for food log and press 2 for exercise log')
        c = int(input())
        if (c == 1):
            print('enter the food eat')
            value = input()
            with open('rohan_food.txt', 'a') as op:
                op.write(str([(str(getdate()))]) + ':' + value + '\n')
            print('sucessfully written')
        elif (c == 2):
            print('enter the exercise')
            value = input()
            with open('rohan_exerc.txt', 'a') as op:
                op.write(str([(str(getdate()))]) + ':' + value + '\n')
            print('sucessfully written')
        else:
            print('wrong option selected')
    elif (z == 3):
        print('press 1 for food log and press 2 for exercise log')
        c = int(input())
        if (c == 1):
            print('enter the food eat')
            value = input()
            with open('hammad_food.txt', 'a') as op:
                op.write(str([(str(getdate()))]) + ':' + value + '\n')
            print('sucessfully written')
        elif (c == 2):
            print('enter the exercise')
            value = input()
            with open('hammad_exerc.txt', 'a') as op:
                op.write(str([(str(getdate()))]) + ':' + value + '\n')
            print('sucessfully written')
        else:
            print('wrong option selected')

def reterive(n):
    if (n==1):
        print('press 1 for food log and press 2 for exercise log')
        c = int(input())
        if(c==1):
            with open('harry_food.txt') as op:
                for i in op:
                    print(i,end='')
        elif(c==2):
            with open('harry_ex.txt') as op:
                for i in op:
                    print(i,end='')
        else:
            print('please choose correct option')
    elif (n==2):
        print('press 1 for food log and press 2 for exercise log')
        c = int(input())
        if(c==1):
            with open('rohan_food.txt') as op:
                for i in op:
                    print(i,end='')
        elif(c==2):
            with open('rohan_ex.txt') as op:
                for i in op:
                    print(i,end='')
        else:
            print('please choose correct option')

    elif (n == 3):
        print('press 1 for food log and press 2 for exercise log')
        c = int(input())
        if (c == 1):
            with open('hammad_food.txt') as op:
               for i in op:
                  print(i, end='')
        elif (c == 2):
            with open('hammad_ex.txt') as op:
               for i in op:
                 print(i, end='')
    else:
        print('please choose correct option')








print('welcome to health management system')
print('press 1 if you want to log data and press 2 if you want to reterive the data')
a=int(input())
if(a==1):
    print('whose log data you want to add press 1.harry 2.rohan 3. hammad')
    b=int(input())
    take(b)
elif(a==2):
    print('whose data you want to reterive press 1.harry 2.rohan 3. hammad')
    b = int(input())
    reterive(b)
else:
    print('wrong input choose correct option')
