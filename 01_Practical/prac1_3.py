i = int(input("Enter a number[1 = Right-angled triangle, 2 = Pyramid]: "))

if i == 1:
    n = int(input("Enter the number of rows: "))
    for i in range(1, n + 1):
        print("*" * i)
elif i == 2:
    n = int(input("Enter the number of rows: "))
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))