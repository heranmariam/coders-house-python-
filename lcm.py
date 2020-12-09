n1=int(input("enter the num1"))
n2=int(input("enter the num2"))
if n1<n2:
    greater=n2
else:
    greater=n1
while (True):
    if greater%n1==0 and greater%n2==0:
        print("lcm is",greater)
        break
    greater+=1
    
