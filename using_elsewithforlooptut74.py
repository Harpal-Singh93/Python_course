# else with for loop works only when the for loop ends normally or
# after all its iteration without any interruption

# 1. case when else executed successfully
# khana=['roti','sabzi','daal','rice']
#
# for i in khana:
#     print(i)
#
# else:
#     print('for loop ended successfully')

# 2. when else not getting executed

khana=['roti','sabzi','daal','rice']

for item in khana:
    if(item=='roti'):
     break
else:
    print('for loop ended successfully')