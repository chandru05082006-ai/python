n = int(input("Enter a 4-digit number: "))

a = n // 1000
b = (n // 100) % 10
c = (n // 10) % 10
d = n % 10

sum = a + b + c + d

print("Sum of digits =", sum)