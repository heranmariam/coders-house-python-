n=int(input("enter the limit"))
k=n
prod=1
while n>=1:
    prod*=n
    n-=1
print("product upto",k,"is",prod)
