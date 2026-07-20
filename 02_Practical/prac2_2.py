#2.2
n = int(input("enter no of element :"))
l = []

for i in range(n) :
  l.append(int(input("enter element :")))

max = l[0]
min = l[0]
for i in range(len(l)) :
  if (l[i] > max):
    max = l[i]
  if(l[i] < min) :
    min = l[i]

unique = list(set(l))

print("list :",l)
print("max value :", max)
print("min value :", min)
print("unique element :",unique)