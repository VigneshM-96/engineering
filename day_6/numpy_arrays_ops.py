import numpy as np 

#creating array
matrix = np.array([[1, 2, 3], [4, 5, 6]])

print("Array Summary :\n")
print("Array Structure :",matrix)

#ndim : number of dimensions
print(f"Number of dimensions : {matrix.ndim}")

#shape : tuple showing size of tuple with (row, column)
print(f"Shape of the arrat : {matrix.shape}")

#dtype : data type of the array elements
print(f"Data type of the array : {matrix.dtype}")