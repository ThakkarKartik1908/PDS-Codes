a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))

c = input("Enter an operator (+, -, *, /): ")

if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    print(a / b)
else:
    print("Invalid operator.")