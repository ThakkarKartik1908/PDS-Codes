import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

corr = iris.corr(numeric_only=True)

sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Iris Dataset')
plt.show()
