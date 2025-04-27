import numpy as np

matrix_np = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

k = 2
# column wise slicing
column_np = matrix_np[:, k]
print(column_np)

# row wise slicing
row_np = matrix_np[k, :]
print(row_np)
