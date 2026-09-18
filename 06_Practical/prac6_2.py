import pandas as pd 
data = { 
'ID': [101, 102, 103, 104], 
'Name': ['Aarav', 'Diya', 'Kabir', 'Isha'], 
'Dept': ['IT', 'HR', 'Finance', 'IT'], 
'Salary': [55000, 48000, 62000, 58000] 
} 
df = pd.DataFrame(data) 
print(df)