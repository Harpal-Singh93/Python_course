var1=2
var2=5
print("enter any value for var 3")
var3=int(input())
if var2>var3:
    print("var3 is lesser than var2")
elif var2==var3:
    print("var3 is equal to var2")

else:
    print(" var3 is greater than var2")

   # in & not in with if statements

list1=[1,2,4,5,7]
print(5 in list1)
if 5 in list1:
    print("5 is in the list")
if 8 not in list1:
    print("8 is not in list")

    #quiz

    print("enter your age")
    age=int(input())
    if age>18:
        print("you are eligible for driving car")
    elif age==18:
        print("you need to give test to qualify for driving")
    else:
        print("you cannot drive you are not eligible")