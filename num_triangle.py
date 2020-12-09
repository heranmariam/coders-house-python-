row=int(input("enter num of rows"))
for i in range(row):
    num=1
    for j in range(i+1):
        print(num,"" ,end="")
        num=num+1
    print("\r")  
