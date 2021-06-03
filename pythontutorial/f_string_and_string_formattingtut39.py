# f strings
import math
#simple case :
# me='harpal'
# a='this is %s'%me
# print(a)

#another way
# me='harpal'
# a1=3
# z='this is %s %s '%(me,a1)
# print(z)

#another way

# me='harpal'
# a1=3
# a='this is {} {}'
# b=a.format(me,a1)
# print(b)

# we can also change the position of above case
# me='harpal'
# a1=3
# a='this is {1} {0}'
# b=a.format(me,a1)
# print(b)

#this is the probably the best way to write above codes
me='harpal'
a1=3
a=f"this is {me} {a1}  {4*5}"
b=f"this is value of cos(60) {math.cos(60)}"
print(a)
print(b)