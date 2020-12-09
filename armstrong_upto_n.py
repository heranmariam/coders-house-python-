n=int(input("enter the limit"))
for i in range(1,n+1):
    k=i
    arm=0
    while i>0:
        d=i%10
        arm=(d**3)+arm
        i=i//10
    if arm==k:
        print(arm)
