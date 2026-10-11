import numpy as np 

arr = np.array([
  [1, 2, 3],
  [4, 5, 6]
])

#indexing
print("First row last element :", arr[0, -1])
print("Second row first element :", arr[1][0])

#slicing
print("First column :", arr[:, 0])