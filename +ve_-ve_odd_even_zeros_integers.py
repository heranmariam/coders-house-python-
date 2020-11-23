n=int(input("enter the size of list"))
i=0
pcount=0
ncount=0
ocount=0
ecount=0
zcount=0
while i<n:
    k=int(input("enter integer"))
    i+=1
    if k>=0:
        pcount+=1
    else:
        ncount+=1
    if k%2==0:
        ecount+=1 
    else:    
        ocount+=1
    if k==0:
        zcount+=1
print("positive numbers:",pcount,"\nnegative numbers:",ncount,"\nodd numbers:",ocount,"\neven numbers:",ecount,"\nzeros are:",zcount)
