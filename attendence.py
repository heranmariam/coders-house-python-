a=int(input("no of class"))
b=int(input("no of class attend"))
attendence=b/a*100
if attendence>=75:
    print("allow to write the exam")
else:
    c=input("medical leave y/n")
    if c=="y":
        print("allow to write the exam")
    else:
        print("not allowed")
