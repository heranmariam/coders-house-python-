a=int(input("enter the num1"))
b=int(input("enter the num2"))
operation=input("enter operation")
if operation=="+":
    print(a+b)
elif operation=="-":
    print(a-b)
elif operation=="*":
    print(a*b)
elif operation=="/":
    if b==0:
        print("not possible")
    else:
        print(a/b)
else:
    print("invalid")  
