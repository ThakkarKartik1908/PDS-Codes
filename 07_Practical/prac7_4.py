import pandas as pd

data = {
   'Region': ['North', 'South', 'North', 'East', 'South', 'East', 'North', 'South'],
   'Product': ['A', 'B', 'A', 'A', 'A', 'B', 'B', 'B'],
   'Sales': [200, 150, 220, 300, 180, 250, 210, 160]
}

df = pd.DataFrame(data)
print(df)

# Average sales by Region and Product
pivot = pd.pivot_table(df, values='Sales', index='Region', columns='Product', aggfunc='mean')
print(pivot)

# Add row and column totals (using sum instead of mean for the margin)
pivot_with_totals = pd.pivot_table(df, values='Sales', index='Region', columns='Product', aggfunc='mean', margins=True)
print(pivot_with_totals)
