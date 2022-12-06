a=int(input("Enter 1 number :"))
b=int(input("Enter 2 number :"))
c=int(input("Enter 3 number :"))
max= a if a>b and a>c else b if b>c else c
print(max)