n1=int(input("enter the num1"))
n2=int(input("enter the num2"))
if n1<n2:
    smaller=n1
else:
    smaller=n2
for i in range(1,smaller+1):
    if n1%i==0 and n2%i==0:
        hcf=i
print("hcf is",hcf)    
