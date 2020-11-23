n=int(input("enter the size of list"))
i=0
y=[]
while i<n:
    k=int(input("enter integer"))
    y.append(k)
    i+=1
k=int(input("number to search"))
i=0
z=0
while i<n:
    if y[i]==k:
        z=1
    i+=1
if z==0:
    print("not present")
else:
    print("present")
