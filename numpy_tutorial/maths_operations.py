import numpy as np

# Element-wise operations
arr = np.array([1, 2, 3])
print(arr + 2)   
print(arr * 3)   
print(arr ** 2)  

# Array-to-array operation
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)  
print(a * b)  

# Useful built-in functions
arr = np.array([1, 2, 3, 4])
np.sum(arr)     
np.mean(arr)    
np.min(arr)     
np.max(arr)     
np.std(arr)     

# Math on 2D arrays
mat = np.array([[1, 2],
                [3, 4]])
np.sum(mat, axis=0)  # column-wise → [4 6]
np.sum(mat, axis=1)  # row-wise → [3 7]
