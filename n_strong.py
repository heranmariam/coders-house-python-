n=int(input("enter the limit"))
for i in range(1,n+1):
    strong=0
    k=i
    while i>0:
        d=i%10
        fact=1
        while d>=1:
            fact*=d
            d-=1
        strong+=fact
        i//=10
    if strong==k:
        print(k)
