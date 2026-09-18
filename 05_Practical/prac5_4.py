import numpy as np

# Generate two random 3x3 matrices
A = np.random.randint(1, 10, size=(3, 3))
B = np.random.randint(1, 10, size=(3, 3))

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix multiplication
result = np.dot(A, B)

print("\nMatrix Multiplication (A × B):")
print(result)

# Transpose of the result
transpose = result.T

print("\nTranspose of Result:")
print(transpose)

# Determinant of the result
determinant = np.linalg.det(result)

print("\nDeterminant of Result:")
print(determinant)