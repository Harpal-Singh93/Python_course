def printhar(string):
  return f'my collegue name is {string}'

def add_num(num1,num2):
  return num1+num2+5
print('the name is ',__name__)     # if we use this statement in this code it will display __main__ here
# but if we run in another file it will show this file name
if __name__ == '__main__':       # this syntax is used to avoid unnecessary execution
  # of below statements in another file when using this file as module
  # it will show if_name_main_usagetut46
    print(printhar('rohan'))
    o=add_num(10,5)
    print(o)
