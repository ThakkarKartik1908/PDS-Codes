#3.1
file = open("input.txt", "r")
data = file.read()
characters = len(data)
words = len(data.split())
lines = len(data.splitlines())
file.close()
find = open("output.txt", "w")
# file only accept string not int
find.write('no of Characters: ' + str(characters) + '\n')
find.write('no of Words: ' + str(words) + '\n')
find.write('no of Lines: ' + str(lines) + '\n')
find.close()