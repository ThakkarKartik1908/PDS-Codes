#2.3
i = input("enter string:")
d = {}

for ch in i :
  if (ch in d) :
    d[ch] = d[ch] + 1
  else:
    d[ch] = 1

for ch in d :
  print(ch ,":",d[ch])