import numpy as np
import random

#create array with elements blw 1 to 100 and 24 elements in shape 6x4
a = np.random.randint(1,100,24).reshape(6,4)

print(a>50) #return boolean matrix
# [[ True  True False False]
#  [ True  True  True False]
#  [False  True False False]
#  [False False  True False]
#  [ True  True  True False]
#  [ True  True  True False]]

print(a[a>50]) #return array with element grater than 50
# [90 77 60 94 64 98 57 93 51 56 74 55 82]
print(a[(a>50) & (a % 2 == 0)]) #return array with element grater than 50 and even 
# [90 60 94 64 98 56 74 82]