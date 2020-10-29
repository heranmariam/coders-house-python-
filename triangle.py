x=int(input("enter the value of x"))
y=int(input("enter the value of y"))
z=int(input("enter the value of z"))
if x==y==z:
	print("Equilateral triangle")
elif x==y or y==z or z==x:
	print("isosceles triangle")
else:
	print("Scalene triangle")
