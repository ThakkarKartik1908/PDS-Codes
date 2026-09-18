import pandas as pd

emp_details = pd.DataFrame({
   'ID': [101, 102, 103, 104],
   'Name': ['Aarav', 'Diya', 'Kabir', 'Isha'],
   'Dept': ['IT', 'HR', 'Finance', 'IT']
})

salary_details = pd.DataFrame({
   'ID': [101, 102, 103, 105],
   'Salary': [55000, 48000, 62000, 60000]
})

# Inner merge (only matching IDs)
merged_inner = pd.merge(emp_details, salary_details, on='ID', how='inner')
print(merged_inner)

# Left merge (all employees, matching salary where available)
merged_left = pd.merge(emp_details, salary_details, on='ID', how='left')
print(merged_left)

# Outer merge (all records from both, matched where possible)
merged_outer = pd.merge(emp_details, salary_details, on='ID', how='outer')
print(merged_outer)

# Using join() with ID set as index
emp_indexed = emp_details.set_index('ID')
salary_indexed = salary_details.set_index('ID')
joined = emp_indexed.join(salary_indexed, how='inner')
print(joined)


