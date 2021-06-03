"""
Exception handling with try, except, else and finally
Try: This block will test the excepted error to occur
Except:  Here you can handle the error
Else: If there is no exception then this block will be executed
Finally: Finally block always gets executed either exception is generated or not
"""

f1=open("test.txt")
try:
    f=open('larry.txt')
except EOFError as a:
    print('Eoferror aa gya hai ',a)
except IOError as a:
    print('IOerror aa gya hai ',a)
except Exception as e:
    print(e)
else:
    print('this will run only if no exception will occur')
finally:
    print('Run this anyway')
    f1.close()

print('Important stuff')
