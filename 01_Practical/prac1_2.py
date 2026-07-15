i = int(input("Enter the number of terms for the Fibonacci series: "))
a, b = 0, 1
z = 0

while z < i:
    print(a, end=" ")
    a = b
    b = a + b
    z += 1