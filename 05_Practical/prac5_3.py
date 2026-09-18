import numpy as np

# 1. np.zeros()
zeros_array = np.zeros(5)
print("Zeros Array:")
print(zeros_array)

# 2. np.ones()
ones_array = np.ones(5)
print("\nOnes Array:")
print(ones_array)

# 3. np.arange()
arange_array = np.arange(1, 11)
print("\nArange Array:")
print(arange_array)

# 4. np.linspace()
linspace_array = np.linspace(0, 10, 5)
print("\nLinspace Array:")
print(linspace_array)

# 5. np.reshape()
array = np.arange(1, 13)
reshaped_array = np.reshape(array, (3, 4))
print("\nReshaped Array:")
print(reshaped_array)