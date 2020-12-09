r=int(input("enter rows "))
for i in range(1,r+1):
    space=r-i
    for j in range(space):
        print(" ",end="")
    for k in range(0,2*i-1):
        print("*",end="")
    print("\r")
