leap=int(input("enter the year"))
if leap%4==0:
    if leap%100==0:
        if leap%400==0:
            print(leap,"is leap year")
        else:
            print(leap,"is not leap year")
    else:
        print(leap,"is leap year")
else:
    print(leap,"is not leap year")
