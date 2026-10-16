import numpy as np

#method 1
a = np.array([1, 2, 3, 4, 5]) #1D array
print(a,'\n')
b=np.array([[1,2,3],[4,5,6]]) #2D array
print(b,'\n')
c=np.array([[1,2,3],[4,5,6],[7,8,9]]) #matrix 
print(c,'\n')

#method 2
d = np.arange(1,11)
print(d,'\n')
d = np.arange(1,11).reshape(5,2) # reshape into 5 rows 2 col
print(d,'\n')

#method 3
d = np.ones((3,4)) #3 rows 4 col
print(d,'\n')

#method 4
d = np.random.random((3,4))
print(d,'\n')

#method 5
d = np.linspace(-10,10,10,dtype = int)
print(d,'\n')

#identity matrix
d= np.identity(3)
print(d,'\n')
