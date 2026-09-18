import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

sns.boxplot(x='day', y='total_bill', data=tips)
plt.title('Distribution of Total Bills by Day')
plt.xlabel('Day')
plt.ylabel('Total Bill')
plt.show()
