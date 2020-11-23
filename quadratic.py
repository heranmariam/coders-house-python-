import math 
a=int(input("enter 1st coeffient"))
b=int(input("enter 2nd coeffient"))
c=int(input("enter 3rd coeffient"))
d=b**2-(4*a*c)
if d==0:
    print(-b/2*a," roots are identical and real")
elif d>0:
    print((-b+math.sqrt(d))/2*a, "," ,(-b-math.sqrt(d))/2*a," roots are distinct and real")
else:
    print(-b/2*a,"+ i",math.sqrt(-d)/2*a, "," ,-b/2*a,"- i",math.sqrt(-d)/2*a,"roots are distinct and imaginary")
