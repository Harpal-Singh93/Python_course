
#function for generating a random signal for snake,water and gun
print('welcome to snake,water and gun game\n')
import random
op=['s','w','g']
z=random.choice(op)
computer_score=0
human_score=0
i=10
while(i>0):

     op = ['s', 'w', 'g']
     comp = random.choice(op)
     print('enter you choice from the following option')
     print('press s for snake','w for water',' g for gun')
     user=input()
     if(user=='s' and comp=='w'):
         print('user wins this time')
         i=i-1
         print('the tries left ',i,'out of 10')
         human_score=human_score+1
         print('you score ',human_score)
         print('computer score is',computer_score)
     elif(user=='w' and comp=='s'):
         print('comp win this time')
         computer_score=computer_score+1
         i = i - 1
         print('the tries left ', i, 'out of 10')
         print('you score ', human_score)
         print('computer score is', computer_score)
     elif (user == 'g' and comp == 'w'):
         print('comp win this time')
         computer_score = computer_score + 1
         i = i - 1
         print('the tries left ', i, 'out of 10')
         print('you score ', human_score)
         print('computer score is', computer_score)
     elif (user == 's' and comp == 'g'):
         print('comp win this time')
         computer_score = computer_score + 1
         i = i - 1
         print('the tries left ', i, 'out of 10')
         print('you score ', human_score)
         print('computer score is', computer_score)
     elif (user == 'g' and comp == 's'):
         print('user wins this time')
         human_score = human_score + 1
         i = i - 1
         print('the tries left ', i, 'out of 10')
         print('you score ', human_score)
         print('computer score is', computer_score)
     elif (user == 'w' and comp == 'g'):
         print('user wins this time')
         human_score = human_score + 1
         i = i - 1
         print('the tries left ', i, 'out of 10')
         print('you score ', human_score)
         print('computer score is', computer_score)
     elif(user==comp):
         print('tie this time')
         i = i - 1
         print('the tries left ', i, 'out of 10')
         print('you score ', human_score)
         print('computer score is', computer_score)
     else:
         print('enter correct case')
         i = i - 1
         print('the tries left ', i, 'out of 10')
         print('you score ', human_score)
         print('computer score is', computer_score)


print('the tries are over lets get to the result')
if(human_score==computer_score):
    print('this is a tie match better luck next time')
    print('human and computer score are ',human_score)
elif(human_score>computer_score):
    print('human can beat the machine')
    print('human score are ',human_score)
    print('computer score are ',computer_score)
    print('human win by ',human_score-computer_score,' scores')
else:
    print('computer wins this time\n')
    print('human score are ', human_score)
    print('computer score are ', computer_score)
    print('computer win by ',computer_score-human_score, ' scores')




