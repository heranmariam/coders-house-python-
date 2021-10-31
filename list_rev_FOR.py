n=int(input("enter the size of list"))
y=[]
for i in range(n):
    k=int(input("enter the integer"))
    y.append(k)
x=y.copy()
x.reverse()
print (x)
