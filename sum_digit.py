num=int(input("Enter a number"))
i=0
while num>0:
    d=num%10
    i=i+d
    num=num//10
print("The sum of num is",i)
