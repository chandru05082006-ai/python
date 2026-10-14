a=int(input("enter first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if a>=b and a>=c:
  largest=a
elif b>=a and b>=c:
  largest=b
else:
  largest=c
print("largest number=",largest)  