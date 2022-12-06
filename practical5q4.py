i=33
j=0
while(i<=126):
    print(chr(i),ord(chr(i)),hex(i),end="  ")
    j=j+1
    i=i+1
    if(j==5):
        print()
        j=0
    
    