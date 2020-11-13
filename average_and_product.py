i=0
prod=1
sum1=0
count=0
while i==0:
    n=int(input("enter the number"))
    prod*=n
    sum1+=n
    count+=1
    a=input("press q to quit")
    if a=="Q" or a=="q":
        i=1
print("product is",prod,"and average is",sum1/count)
