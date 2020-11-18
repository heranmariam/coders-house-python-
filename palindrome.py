n=int(input("enter the number"))
k=n
i=0
while n>0:
    d=n%10
    i=i*10+d
    n=n//10
if i==k:
    print("palindrome")
else:
    print("not palindrome")
