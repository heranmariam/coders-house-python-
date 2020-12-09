n=int(input("Enter any limit"))
for i in range(1,n+1):
    perfect=0
    div=1
    while div<i:
        if i%div==0:
            perfect=perfect+div
        div+=1
    if perfect==i:         
        print(i)
