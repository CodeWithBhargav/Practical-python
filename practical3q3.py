p=int(input("Enter P"))
r=int(input("Enter R"))
n=int(input("Enter N"))
t=int(input("Enter T"))


print('simple interest :: ',(p*r*n)/100)
print('Compound interest :: ',p*(1+r/100*n)**n*n)