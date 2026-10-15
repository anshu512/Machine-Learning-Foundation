import numpy as np

np.random.seed(0)

x1= np.random.randint(10, size=6) #1d array
x2 = np.random.randint(10, size=(3,4)) #2d array
x3 = np.random.randint(10, size=(3,4,5)) #3d array

#Array Attributes
print(x3.ndim) #ndim -> no of dimentions
print(x3.shape) #shape -> size of each dim
print(x3.size) #size -> total size of array
print(x3.dtype) # data type of the array
print(x3.itemsize) #size of each array element in bytes
print(x3.nbytes) #total size of array in bytes

#Array indexing
print(x1[0]) #1d array has normal indexing
print(x2[0,0]) #2d array has matrix like indexing
print(x3[0,0,0]) #3d array is complex

#Fancy Indexing
print(x2[[0,2]]) #we get 1st row and 3rd row
print(x2[:,[0,2]]) #we get 1st col and 3rd col

#Boolean Indexing


x1[0] = 3.14 # if array if int and you insert floating value then value will be truncated silently.

#Array slicing
print(x1[::-1]) #in 1d array slicing work like normal python list
print(x2,'\n',x2[::-1,::-1]) #in 2d array slicing work seperately for rows and column

#Subarray
print("Sub Array")
print(x2)
x2_sub = x2[:2, :2] #subarray with 1st 2 rows and 1st 2 colums
print(x2_sub) 
# x2_sub[0,0] = 12 #changing subarry chages the original array
# print(x2)

#Creating copy of array
x2_sub_copy = x2[:2,:2].copy()
print(x2_sub_copy) #changing this sub arry will not change the original

#Reshaping of Arrays only work when initail size is same as final size
grid = np.arange(1,10) #1d array form 1 to 9 ,size = 9
print(grid.reshape(3,3)) #reshape to 3x3 matrix ,size = 3x3 = 9

#Reshape using newaxis
x=np.array([1,2,3])
print(x[np.newaxis, :]) #row vector
print(x[:, np.newaxis]) #column vector

#Concatination
x=np.array([1,2,3])
y=np.array([3,2,1])
print(np.concatenate([x,y])) #[1,2,3,3,2,1]

#Concatenate in 2D
grid = np.array([[1,2,3],[4,5,6]]) #2d matrix
print(np.concatenate([grid,grid])) #2x3 -> 4x3 (concate along colms axis = 0)
print(np.concatenate([grid, grid],axis=1)) #2x3 -> 2x6  (concate along rows axis = 1)

#vertical staking (concatinating array of diff dim)
x = np.array([1,2,3])
grid = np.array([[4,5,6],[7,8,9]])
print(np.vstack([x,grid]))

#Horizontal staking
y= np.array([[33],
             [44]])
print(np.hstack([grid, y]))
