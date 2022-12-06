n=int(input("Enter How Many Number : "))
li=[]
for i in range(n):
	e=int(input("Enter  Number : "))
	li.append(e)
for i in li:
	for j in li:
		print(i,j,end="  ")
	print()
print("Total Combinations :: ",n*n)
