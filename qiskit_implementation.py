# In Python, matrix and vector computations can be performed
# using the array class from NumPy Library
import numpy as np

# Define two column vectors ket0 and ket1
# Corresponding to the qubit state vectors |0> and |1>
# and print their average 
ket0 = np.array([[1], [0]])
ket1 = np.array([[0], [1]])

print(ket0 / 2 + ket1 / 2)

# Use an Array to create matrices that can represent operations
M1 = np.array(([[1, 1], [0, 0]]))
M2 = np.array(([[1, 0], [0, 1]]))

M = M1 / 2 + M2 / 2
print(M)

# Matrix multiplication, including matrix-vector multiplication
# can be performed using the @ operator
print(M1 @ ket1)
print(M1 @ M2)
print(M @ M)
