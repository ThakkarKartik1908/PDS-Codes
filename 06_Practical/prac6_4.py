import pandas as pd 
data = { 
'ID': [101, 102, 103, 104], 
'Name': ['Aarav', 'Diya', 'Kabir', 'Isha'], 
'Dept': ['IT', 'HR', 'Finance', 'IT'], 
'Salary': [55000, 48000, 62000, 58000] 
} 
df = pd.DataFrame(data) 
# Select specific columns using .loc 
print(df.loc[:, ['Name', 'Salary']]) 
# Select specific columns using .iloc 
print(df.iloc[:, [1, 3]]) 
# Filter rows where Salary > threshold using .loc 
threshold = 55000 
print(df.loc[df['Salary'] > threshold]) 
# Combine column selection and row filtering with .loc 
print(df.loc[df['Salary'] > threshold, ['Name', 'Salary']]) 
# Filter using .iloc with boolean mask converted to positions 
print(df.iloc[(df['Salary'] > threshold).values])