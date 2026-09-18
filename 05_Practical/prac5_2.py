#p5.2
import numpy  as np

matrix  = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])


print("Original Matrix:")
print(matrix)

print("\n2nd Row:")
print(matrix[1,:])

print("\n3rd col:")
print(matrix[:2])

matrix[matrix % 2 == 0] = -1

print("\nMatrix after replacing even numbers with -1:")
print(matrix)