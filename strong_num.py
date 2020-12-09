n=int(input("enter the num"))
k=n
strong=0
while n>0:
    d=n%10
    fact=1
    while d>=1:
        fact*=d
        d-=1
    strong+=fact
    n//=10
if strong==k:
    print("is a strong number")
else:
    print("not a strong number")
