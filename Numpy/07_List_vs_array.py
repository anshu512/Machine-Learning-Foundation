import time
import numpy as np
import sys

#Speed comparision
a = [i for i in range(10000000)]
b = [i for i in range(10000000, 20000000)]

c=[]
start = time.time()
for i in range(len(a)):
    c.append(a[i] + b[i])    
print(time.time() - start)

x1=np.arange(10000000,dtype = np.int32)
x2=np.arange(10000000,20000000)
start = time.time()
x= x1 + x2
print(time.time()-start)

#-------Memory comparision---------
print(sys.getsizeof(a)) #size of list with 1 crore items
print(sys.getsizeof(x1)) #size of numpy arrray with 1 crore items
