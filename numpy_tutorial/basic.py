import numpy as np

arr=np.array([[1,2,3,4,5]],np.int64)
print(arr)
print(arr[0,1])
print(arr.shape)
print(arr.dtype)
arr[0,1]=45
print(arr)