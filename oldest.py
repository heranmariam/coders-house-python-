a=int(input("enter the first age"))
b=int(input("enter the second age"))
c=int(input("enter the 3rd age"))
if a>b and a>c:
    print(a,"is oldest")
elif b>a and b>c:
    print(b,"is oldest")
else:
    print(c,"is oldest")
if a<b and a<c:
    print(a,"is youngest")
elif b<a and b<c:
    print(b,"is youngest")
else:
    print(c,"is youngest")
