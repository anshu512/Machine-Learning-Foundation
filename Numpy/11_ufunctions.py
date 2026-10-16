import numpy as np

#Array arithmetic operations are applied on all elements

x=np.arange(4)
print('x   =',x)
print('x + 5=',x + 5)
print('x * 2=',x * 2)

#there are functions for these operations

print(np.add(x,2)) #add 2 to every element of x
print(np.power(x,2)) #every element power 2
print(np.exp(x)) # e^ every elemet

#we can save the ouput value after computation
y = np.empty(4, dtype=np.int16) #empty array of size 4
np.add(x,2,out=y) # the result is stored in y
print(y)

#Reduce function- apply same arithmetic operatoin until single element remains
print("x  =", x)
print(np.add.reduce(x)) #sum each element
print(np.multiply.reduce(x)) #multiply each element
print(np.add.accumulate(x)) #store every intermediate result

#outer products
#create matrix of every pair of possible operations
x= np.arange(1,7) # dies with 1 to 6
print(np.add.outer(x,x))
#create matrix with every possible sum pair
# [[ 2  3  4  5  6  7]
#  [ 3  4  5  6  7  8]
#  [ 4  5  6  7  8  9]
#  [ 5  6  7  8  9 10]
#  [ 6  7  8  9 10 11]
#  [ 7  8  9 10 11 12]]

