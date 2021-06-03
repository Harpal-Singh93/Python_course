#program for selecting only odd places item

#traditional way using if and for loop and incrementing the variable

# l1=['bhindi','aloo','chopsticks','chowmein']
# i=1
# for item in l1:
#     if i%2 != 0:
#      print(f'jarvis please buy {item}')
#     i+=1

# we can do this thing easily with the help of enumerate function

l1=['bhindi','aloo','chopsticks','chowmein']

for index,item in enumerate(l1):
  if index%2==0:      # we appiled the condition of 0 here because index start with 0
    print(f'jarvis please buy {item}')
