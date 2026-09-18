import pandas as pd
import matplotlib.pyplot as plt

data = {
   'Age': [22, 25, 28, 22, 35, 40, 45, 30, 28, 25, 33, 38, 42, 27, 29, 31, 36, 24, 26, 39]
}

df = pd.DataFrame(data)

plt.hist(df['Age'], bins=8, color='skyblue', edgecolor='black')
plt.title('Distribution of Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


