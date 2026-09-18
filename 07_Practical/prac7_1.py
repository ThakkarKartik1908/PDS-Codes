import pandas as pd
import numpy as np

data = {
   'ID': [101, 102, 103, 104, 105],
   'Name': ['Aarav', 'Diya', 'Kabir', 'Isha', 'Rohan'],
   'Dept': ['IT', 'HR', np.nan, 'IT', 'Finance'],
   'Salary': [55000, np.nan, 62000, 58000, np.nan]
}

df = pd.DataFrame(data)
print(df)

# Drop rows with any NaN values
df_dropped = df.dropna()
print(df_dropped)

# Fill NaN in Salary with mean
df_mean = df.copy()
df_mean['Salary'] = df_mean['Salary'].fillna(df_mean['Salary'].mean())
print(df_mean)

# Fill NaN in Salary with median
df_median = df.copy()
df_median['Salary'] = df_median['Salary'].fillna(df_median['Salary'].median())
print(df_median)

# Fill NaN in Dept with a placeholder
df_dept = df.copy()
df_dept['Dept'] = df_dept['Dept'].fillna('Unknown')
print(df_dept)

