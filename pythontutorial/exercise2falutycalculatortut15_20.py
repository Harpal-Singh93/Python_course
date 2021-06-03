print("enter the  which operation you want to perform between +,-,*,/")
ch=input()
print("enter first number")
var1=int(input())
print("enter second number")
var2=int(input())
if ch=='+':
    if (var1==56 and var2==9)or ( var1==9 and var2==56):
        print("77")
    else:
       print(var1+var2)
elif ch=='*':
    if (var1==45 and var2==3)or ( var1==3 and var2==45):
        print("555")
    else:
       print(var1*var2)
elif ch=='/':
    if (var1==56 and var2==6):
        print("4")
    else:
       print(var1/var2)