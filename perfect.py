n=int(input("Enter any number"))
perfect=0
for i in range(1,n):
    if n%i==0:
        perfect=perfect+i
        # print(i) venamekil print cheytha mathi
if perfect==n:
    
    print("is a perfect num")
else:
    print("not a perfect num")        
    
# do perfect upto n
