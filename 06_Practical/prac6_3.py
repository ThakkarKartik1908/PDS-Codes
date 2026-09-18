import pandas as pd 
df = pd.read_csv('IRIS.csv') 
print(df.head()) 
print(df.tail()) 
print(df.info()) 
print(df.describe()) 
print(df.shape)