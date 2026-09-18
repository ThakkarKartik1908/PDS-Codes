#practical 4.2
import numpy as np

Math = [75, 80, 65, 90, 85, 70, 95, 88, 78, 82]
Science = [70, 85, 60, 92, 80, 72, 90, 86, 75, 84]
# is store in matrix like and we want math and science so that 0 and 1
Correlation_Matrix = np.cov(Math , Science)[0][1]

Correlation_Coefficient = np.corrcoef(Math , Science)[0][1]
print("Maths Score = ", Math)
print ("Science Score = ", Science)
print("Correlation_Matrix = ", Correlation_Matrix)
print("Correlation_Coefficient = ", Correlation_Coefficient)