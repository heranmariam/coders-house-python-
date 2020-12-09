n=int(input("enter the limit"))
for i in range(2,n+1):
    j=2
    k=0
    while j<i:
        if i%j==0:
            k=1
        j+=1
    if k==0:
        print(i)
    
