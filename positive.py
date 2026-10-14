n=int(input("enter how many numbers:"))
positive=0
negative=0
zero=0
for i in range(n):
  num=int(input("enter a number"))
  if num>o:
    positive+=1
  elif num<0:
    negative+=1
  else:
    zero+=1
print("positive numbers=",positive)
print("negative numbers=",negative)
print("zeros=",zero)