import numpy as np
# Generate the same dataset every time with same seed
# The modern best practice (NumPy 1.17+)
rng = np.random.default_rng(42)
x = rng.integers(100, size=10) # Note: 'randint' was renamed to 'integers' here
y = rng.integers(10,size=10)
print("Modern RNG:", x)
print(y)

#combined indexing
x = rng.integers(1,50,size=20).reshape(4,5)
print(x)
# [[25 19  9 46 39]
#  [32 20 41 27 22]
#  [23 12  5 28 44]
#  [ 4 43 41 14 31]]
row = np.array([0,1,3])
col= np.array([0,1,3])
print(x[row,col]) #result in pair valus of x[0,0], x[1,1], x[3,3]
#this is done through broadcasting rules

print(x[row[:, np.newaxis],col])
#create a 3x3 submatrix with cross product of [0,1,3] x [0,1,3]
# [[25 19 46]
#  [32 20 27]
#  [ 4 43 14]]

#combine fancy and simple indecies
print(x[2,[1,2,3]]) #row 2 col 1,2,3 

#combine fancy and slicing
print(x[1:,[1,2,3]]) #for every row get the col values at 1,2,3

#combine fancy and masking
mask = np.array([1,0,1,0,1],dtype=bool) #creating a mask array [ture,false,true,false]
row = np.array([0,1,3])

print(x[row[:,np.newaxis],mask])
#[[25  9 39]  #row 0 keep those col which has ture i.e 0,2,4
#  [32 41 22]
#  [ 4 41 31]]

#Modifing values using fancy indexing
x = np.arange(10)
i = np.array([2,1,8,4])
x[i]=99
print(x) #[ 0 99 99  3 99  5  6  7 99  9]

x[i] -= 10
print(x) #[ 0 89 89  3 89  5  6  7 89  9]

#repeated indicis can cause unexpected results
x= np.zeros(10)
i = [0,0]
x[i] = [4,6]
print(x) #[6. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# x[0] = 4 then x[0] = 6 so final result contain 6

i = [2,3,3,4,4,4]
x[i] += 1 # expected [6 0 1 2 3 0 0 0 0 0]
print(x) # result [6. 0. 1. 1. 1. 0. 0. 0. 0. 0.]
#it simply overwrites the exact same value multiple times.

#to get the desire result 
np.add.at(x,i,1)
print(x) #[6. 0. 2. 3. 4. 0. 0. 0. 0. 0.]