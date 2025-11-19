import numpy as np

x=[[1,2,3],[2,3,4],[1,2,1]]
arr=np.array(x)
print(x)
print(arr.sum(axis=0))#asis=0 means row
print(arr.sum(axis=1))#axis=1 means column
print(arr.T)
arr.flat
for i in arr.flat:
    print(i)
#print(arr.argsort())#it sort the rows and columns not the values in it
print(np.sort(arr))