import os
try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide a number by zero.")

filename = "sample.txt"

try:
    print("Python is looking in:", os.getcwd())
    file = open(filename, "r")
    content = file.read()

    print("\nFile Name:", filename)
    print("File Content:")
    print(content)

    file.close()

except FileNotFoundError:
    print("Error: File", filename, "not found.")

