#2.4
def get_marks(i) :
  return i[1]

d = {}
s = int(input("enter student no :"))
for i in range(s) :
  n = input("enter name :")
  m = int(input("enter marks:"))
  d[n] = m

descending_dictionary = dict(sorted(d.items(),key = get_marks,reverse = True))

print("input dictionary :",d)
print("descending_dictionary:",descending_dictionary)