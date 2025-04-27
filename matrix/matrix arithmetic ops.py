import numpy as np

# addition
X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

result = np.array(X) + np.array(Y)

# multiplication

A = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]

r = np.dot(A, B)
print(r)
