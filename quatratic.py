import cmath
a=int(input("Enter a"))
b=int(input("Enter b"))
c=int(input("Enter c"))
q=(b*b)-(4*a*c)
root1=-b+cmath.sqrt(q)/(2*a)
root2=-b-cmath.sqrt(q)/(2*a)
print("Root 1:",root1)
print("Root 2:",root2)