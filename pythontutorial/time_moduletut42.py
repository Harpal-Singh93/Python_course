# for calculating the execution time of a program
# in this case we are comparing the execution time of for loop and while loop

import time
intial=time.time()
k=0
while(k<45):
   print('hello')
   time.sleep(2)
   k+=1
print('while loop has taken ',time.time()-intial,'seconds')

intial2=time.time()
for i in range(45):
       print('bye')
print('the for loop running time is ',time.time()-intial2,'seconds')


# for printing local time
# localtime=time.asctime(time.localtime(time.time()))
# print(localtime)

# time.sleep(n)  this method is used for adding a delay of n second