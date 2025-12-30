"""
WHen all the length of the sides of the triangle is known -a,b,c
demi perimeter (s) = (a + b + c)/2
Area = s*(s-a)*(s-b)*(s-c)**0.5
"""
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

s = (a+b+c)/2
Area = s*(s-a)*(s-b)*(s-c)**0.5


print("Area of the triangle: ", round(Area,2))
