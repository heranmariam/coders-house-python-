a=int(input("enter the 1st side"))
b=int(input("enter the 2nd side"))
c=int(input("enter the 3rd side"))
if ((a+b)>c) or ((b+c)>a) or ((c+a)>b) :
    print("is a Valid Triangle")
else:
    print("is not valid Triangle")
