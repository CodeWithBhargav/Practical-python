n=int(input("Enter  Number :: "))
k=n+1
for i in range(n+1):
    k=k-1
    for j in range(k):
        print(end=" ")
    for j in range(i):
        print("*",end=" ")
    print()