import numpy as np
import random

x=np.random.randint(1,10,9).reshape(3,3)

print("X   =",x)
# X   = [[2 5 6]
#        [6 2 9]
#        [1 6 7]]

#comparison operations
print(x > 5) #return a boolean matrix 
# [[False False  True]
#  [ True False  True]
#  [False  True  True]]

#How many values are grater than 5
print(np.sum(x > 5)) # true = 1 so it sum them
 
#How many values are grater than 5 in each row
print(np.sum(x > 5, axis=1))

#np.any np.all
print(np.any(x > 5)) #are there any value grater than 5
print(np.all(x < 5)) #all values less than 5

#complex comparison
print(np.sum((x > 5) & (x%2==0))) # return no of values grater than 5 and even

#Masking Operation 
#if we want to select these valus 
print(x[x > 5]) #returns a 1d array filled with these values 
