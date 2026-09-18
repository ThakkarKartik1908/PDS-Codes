import pandas as pd
import matplotlib.pyplot as plt

data = {
   'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
   'Sales': [12000, 15000, 13000, 17000, 16000, 19000, 21000, 20000, 22000, 24000, 23000, 26000]
}

df = pd.DataFrame(data)

plt.plot(df['Month'], df['Sales'], marker='o', label='Monthly Sales')
plt.title('Monthly Sales of the Company')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.show()
