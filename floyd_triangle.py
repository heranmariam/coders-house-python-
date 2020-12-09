row=int(input("enter num of rows"))
num=1
for i in range(row):
    for j in range(i+1):
        print(num," ",end=' ')
        num=num+1
    print("\r")
