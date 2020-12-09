n=int(input("enter limit"))
k=n
prod=1
for i in range(n,1,-1):
    prod*=i
print("product upto",k,"is",prod)
