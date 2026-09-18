#practical 4.3
import random
import matplotlib.pyplot as plt

f = [0,0,0,0,0,0] # for 6 side

for i in range(1000):
  roll = random.randint(1,6)
  f[roll-1] += 1

print("Frequency Distribution:")

for i in range(6):
    print("Outcome", i + 1, ":", f[i])

x = [1,2,3,4,5,6] #face

plt.bar(x,f)
plt.xlabel("Die Outcome")
plt.ylabel("Frequency")
plt.title("Frequency Distribution of Die Rolls")
plt.show()
