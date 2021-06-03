"""
******* Function caching ********
Function caching allows us to cache the return values of a function depending on the arguments.
It can save time when an I/O bound function is periodically called with the same arguments.
Before Python 3.2 we had to write a custom implementation. In Python 3.2+
there is an lru_cache decorator which allows us to quickly cache and uncache the return values of a function.
"""
# without using lru_cache
# import time
# def some_work(n):
#     # some task taking n seconds
#     time.sleep(n)
#     return n
#
# if __name__=='__main__':
#     print('Now running some work')
#     some_work(3)
#     print('Done... calling again')
#     some_work(3)   # this will again take 3 seconds this issue needs to be resolved
#     print('Called again')


# with using lru_Cache

import time
from functools import lru_cache

@lru_cache(maxsize=3)
def some_work(n):
    # some task taking n seconds
    time.sleep(n)
    return n

if __name__=='__main__':
    print('Now running some work')
    some_work(3)
    # some_work(4)
    # some_work(5)  after these 3 statement it will again take 3 seconds for next some_work(3)
    # some_work(6)  call because for max size =3 it can store only last 3 calls
    # so to avoid it we have to increase max size

    print('Done... calling again')  # now this and below cal don't take there seconds again
    some_work(3)   # as three value are stored in cache memory
    print('Called again')
