import numpy as np
M1 = np.array([[5, 5],
               [1, 2]])

M2 = np.array([[0, 1],
               [1, 0]])
M = np.dot(M1, M2)
M_T = M.T
print("Matrix M1:\n", M1)
print("Matrix M2:\n", M2)
print("Resultant matrix (M1 x M2):\n", M)
print("Transpose of resultant matrix:\n", M_T)