n=int(input("Enter Number : "))
for i in range(1,n+1):
	for j in range(1,n+1):
		print(i,j,end="  ")
	print()
print("Total Combinations :: ",n*n)
