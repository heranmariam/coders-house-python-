num=int(input("Enter any number"))
k=0
for i in range(2,num):
    if num%i==0:
        k=1  
if k==0:
    print("prime")
else:
    print("not prime")
