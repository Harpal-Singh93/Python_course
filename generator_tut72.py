"""
1. ####Iterable####:  An object is called iterable if we can get an iterator from it.
Most built-in containers in Python like: list, tuple, string etc. are iterables.
The iter() function (which in turn calls the __iter__() method) returns an iterator from them.
__getitem__ is used with this.

2.####Iterator####:Iterator in Python is simply an object that can be iterated upon.
An object which will return data, one element at a time.
Technically speaking, a Python iterator object must implement
two special methods, __iter__() and __next__(), collectively called the iterator protocol.

3.### iteration ###:-Repeated execution of a set of statements is called iteration


4. Generator:Python generators are a simple way of creating iterators.
Simply speaking, a generator is a function that returns an object (iterator)
which we can iterate over (one value at a time).

Create Generators in Python
It is fairly simple to create a generator in Python. It is as easy as defining a normal function,
but with a yield statement instead of a return statement.
"""

# generator function
def gen(n):
    for i in range(n):
        yield i
        #return i

g=gen(3) # g is a generator object now so we can iterate it
print(g)

# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
#print(g.__next__())# this will give error because there is no number ahead

# but instead of generator if we use for loop it doesn't give error because
#for loop handle the exception internally
for i in range(3):
    print(i)

# now using a string for
ch='harry'
# for i in ch:
#     print(i)    # we can do this similar task by making it iterable
z=iter(ch)
print(z.__next__())
print(z.__next__())

# we can use iter() function only on iterable object if ch=8 this will give error
# as integer is not iterable object.
