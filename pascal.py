n=int(input("enter the limit "))
value=[[0 for i in range (n)]for i in range (n)]
for i in range(n): 
    for j in range(n-i):
        print(" ",end="")
    for k in range(i+1):
        if k==0 or k==i:
            value[i][k]=1 
            print(value[i][k],"",end="")
        else:
            value[i][k]=value[i-1][k-1]+value[i-1][k]
            print(value[i][k] ,"",end="")
    print("\r")
print(value)
