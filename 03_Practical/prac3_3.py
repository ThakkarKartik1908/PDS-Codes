import json

# Open and read the JSON file
with open("books.json", "r") as file:
    books = json.load(file)

# Display book details
print("Book Details:")
print("-----------------------------")

for book in books:
    print("Title :", book["Title"])
    print("Author:", book["Author"])
    print("Price :", book["Price"])
    print("-----------------------------")