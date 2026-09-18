import pandas as pd 
data = { 
'Region': ['North', 'South', 'North', 'East', 'South', 'East', 
'North'], 
'Salesperson': ['Aarav', 'Diya', 'Aarav', 'Kabir', 'Diya', 'Isha', 
'Rohan'], 
'Profit': [5000, 3000, 4500, 6000, 3500, 5500, 4000] 
} 
df = pd.DataFrame(data) 
print(df) 
# Total profit per Region 
total_profit_region = df.groupby('Region')['Profit'].sum() 
print(total_profit_region) 
# Average profit per Salesperson 
avg_profit_salesperson = df.groupby('Salesperson')['Profit'].mean() 
print(avg_profit_salesperson) 