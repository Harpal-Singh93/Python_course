import random
import sklearn     # installation using pip install in console
random_number=random.randint(0,5)   # this will print a random integer from 0 to 5
print(random_number)

rand=random.random()  *100
print(rand)   # this will give a random number between 0 and 1  to get under 100 we can multiply it with 100

lst=['star plus','dd national','pogo','zee news']
choice=random.choice(lst)
print(choice)




# search any two module and use its two functions

#!/usr/bin/env python3
# Import playsound module
from playsound import playsound

# Input an existing wav filename
wavFile = input("Enter a wav filename: ")
# Play the wav file
playsound(wavFile)

# Input an existing mp3 filename
mp3File = input("Enter a mp3 filename: ")
# Play the mp3 file
playsound(mp3File)



# statistics module
import statistics

# Calculate average values
print(statistics.mean([1, 3, 5, 7, 9, 11, 13]))

import math

#Round a number upward to its nearest integer
print(math.ceil(1.4))
print(math.ceil(5.3))
print(math.ceil(-5.3))
print(math.ceil(22.6))
print(math.ceil(10.0))



# Return the base-10 logarithm of different numbers
print(math.log10(2.7183))
print(math.log10(1000))