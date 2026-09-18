#parctical 4.4
import random
trials = 1000
aces = 0

for i in range(trials) :
  card = random.randint(1,52)
  # assume card 1 2 3 4 represent the four ace
  if card <= 4  :
     aces += 1

probability = aces / trials
print ("Number of trials = ", trials)
print("Number of aces = ", aces)
print("Probability of drawing an ace = ", probability)
print("Persentage = ",probability*100,"%")