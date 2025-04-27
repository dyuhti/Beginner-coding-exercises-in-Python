import numpy as np

# Define two matrices
matrix_a = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrix_b = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])

# Addition of matrices
matrix_sum = matrix_a + matrix_b

# Subtraction of matrices
matrix_diff = matrix_a - matrix_b

# Sum of diagonal elements
diagonal_sum_a = np.trace(matrix_a)
diagonal_sum_b = np.trace(matrix_b)

# Print the results
print("Matrix A:")
print(matrix_a)

print("\nMatrix B:")
print(matrix_b)

print("\nMatrix Sum:")
print(matrix_sum)

print("\nMatrix Difference:")
print(matrix_diff)

print("\nDiagonal Sum of Matrix A:", diagonal_sum_a)
print("Diagonal Sum of Matrix B:", diagonal_sum_b)

# Sum of elements in each row
row_sums = np.sum(matrix_a, axis=1)
print(row_sums)

# Sum of elements in each column
column_sums = np.sum(matrix_a, axis=0)
print(column_sums)

