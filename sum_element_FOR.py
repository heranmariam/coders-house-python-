n=int(input("enter the size of list"))
y=[]
sum1=0
for i in range(n):
    k=int(input("enter integer"))
    y.append(k)
    sum1+=k
print("the list is",y,"\nand the sum is",sum1)
