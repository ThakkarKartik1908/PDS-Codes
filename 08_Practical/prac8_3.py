import pandas as pd
import matplotlib.pyplot as plt

data = {
   'Study_Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
   'Exam_Score': [35, 42, 50, 55, 63, 68, 75, 80, 88, 92]
}

df = pd.DataFrame(data)

plt.scatter(df['Study_Hours'], df['Exam_Score'], color='blue')
plt.title('Study Hours vs Exam Score')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.show()