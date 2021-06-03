#operator in python

#1.Arithmetic operator
#  +,-,*,%,/,//,**
#let us discuss some of the new one's

#  / division  float
a=5
b=3
print(a/b)

# // division (floor)
print(a//b)

#  ** power operator
print(a**b)

#2. Relational operator
#   >,<,<=,>=,==,!=
print(a!=b)

#3. logical operator

#and,or,not

print(not 0)
print(not 1)
print(True and True)
print(True and False)

#4. Bitwise operator

#  &,|,~,^,>>,<<

print(a&b)
print(a|b)
print(a>>2)
print(a<<1)

#5. assignment operator

#  +=,-=,*=,/=,%=,=,//=,**=,&=,>>=
a+=b   # a is 5 and b is 3
print(a)
a//=b    # a is 8 and b is 3
print(a)
a**=b    # a is 2 and b is 3
print(a)

#6. Identity  operator

# is and is not
#these are used to check the values are located in same part of the memory
#list and mutable and the interpreter declare them in memory at different locaton
a1=3
b1=3
a2='Harpal'
b2='Harpal'
a3=[1,2,3]
b3=[1,2,3]
print(a1 is not b1)
print(a2 is b2)
print(a3 is b3)  # this is false due to above reason

#7. membership operator
# in and not in
# they are used to test whether a value or variable is found in a sequence or not
x='Geeks for Geeks'
y={3:'a',4:'b'}
print('G' in x )
print('geeks'not in x)
print('Geeks' not in x)
print(3 in y)
print('b' in y)  # it will detect the value of dictionary is that way it is showing false