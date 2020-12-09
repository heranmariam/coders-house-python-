n=int(input("enter the size of list"))
y=[]
for i in range(n):
    k=int(input("enter integer"))
    y.append(k)
k=int(input("number to search"))
if k in y:
    print ("present")
else:
    print (" not present")
