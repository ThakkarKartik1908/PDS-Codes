import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
   'Student': ['Aarav', 'Diya', 'Kabir', 'Isha', 'Rohan'],
   'Math': [85, 72, 90, 68, 78],
   'Science': [80, 75, 88, 74, 82]
}

df = pd.DataFrame(data)

x = np.arange(len(df['Student']))
width = 0.35

plt.bar(x - width/2, df['Math'], width, label='Math')
plt.bar(x + width/2, df['Science'], width, label='Science')

plt.title('Math vs Science Marks Comparison')
plt.xlabel('Student')
plt.ylabel('Marks')
plt.xticks(x, df['Student'])
plt.legend()
plt.show()
