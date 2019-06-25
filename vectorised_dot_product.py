import numpy as np
import time

a = np.random.rand(100000)
b = np.random.rand(100000)

tic= time.time()
c= np.dot(a,b)
toc= time.time()
print(c)
print("time taken dot:"+ str(1000*(toc-tic))+"ms")

c=0
tic= time.time()
for i in range(10000):
    c+= a[i]*b[i]
    
toc= time.time()

print(c) 
print("time taken for:"+ str(1000*(toc-tic))+"ms")
