"""
Coroutines are generalization of subroutines. They are used for cooperative multitasking
where a process voluntarily yield (give away) control periodically or
when idle in order to enable multiple applications to be run simultaneously.
In Python, coroutines are similar to generators but with few
extra methods and slight change in how we use yield statement.
Generators produce data for iteration while coroutines can also consume data.
"""

import time

def searcher():
    # some 4 second time taking task
    book='hello my name is harpal.i am software engineer by profession'
    time.sleep(4)

    while(True):
        text=(yield)
        if text in book:
            print('you text is in book')
        else:
            print('you text is not in book')

search=searcher()
next(search)
search.send("harpal")
input('press any key\n')
search.send('software engineer')
input('press any key\n')
search.send('am')
search.close()  # we can close this also and after that if we again try to call it will give error
#search.send('hi') it will give error
