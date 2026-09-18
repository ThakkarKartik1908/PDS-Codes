import pandas as pd

# From a list
s1 = pd.Series([10, 20, 30, 40, 50])
print(s1)

# From a dictionary
s2 = pd.Series({'a': 100, 'b': 200, 'c': 300, 'd': 400})
print(s2)

# Slicing
print(s1[1:4])
print(s2['b':'d'])

# Basic arithmetic
print(s1 + 5)
print(s1 * 2)
print(s2 - 50)
print(s1[:3] + s1[2:5])





