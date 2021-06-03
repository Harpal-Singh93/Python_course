num=20
count=1
left_tries=5
while True:
    print('enter your guess')
    a=int(input())
    if num>a:
        print("you entered a lower number")
        count=count+1
        left_tries=left_tries-1
        print("the tries left are ",left_tries)
    elif num<a:
        print("you have entered a bigger number")
        count=count+1
        left_tries = left_tries - 1
        print("the tries left are ", left_tries)
    else:
        print('you have guessed it right')
        print("you have gussed in ",count,'number of gusses')
        break
    if count==5:
        print("game over")
        break