
print("Enter (F) for fahrenhit to celcius")
print("Enter (C) for celcius to fahrenhit")
which=input("Enter selection:")
temp=int(input("Enter Temprature:"))
if which=='F':
	con_temp=(temp-32)*5/9
	print(temp,"degree fahrenhit equal to ",con_temp," degree celcius")
else:
	con_temp=(temp*9/5)+32
	print(temp,"degree celcius equal to ",con_temp," degree fahrenhit")