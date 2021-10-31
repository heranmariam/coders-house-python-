num=int(input("Enter any num"))
k=num
arm=0
while num>0:
    d=num%10
    arm=(d**3)+arm
    num=num//10
if arm==k:
    print("armstrong")
else:
    print("not armstrong")
