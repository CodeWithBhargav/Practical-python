p,n,o,e,sum,zero=0,0,0,0,0,0
li=[]
import os
os.system("cls")
n1=int(input("Enter How many Number :: "))
for i in range(n1):
    ele=int(input("Enter number::"))
    li.append(ele)

while 1:
    os.system("cls")
    print('''
    1. Positive No
    2. Negative
    3. Odd
    4. even
    5. 0's
    6. Average
    7. Exit''')
    ch=int(input("Enter Choise :: "))

    if (ch==1):
        print("Positive Numbers :: ")
        for i in li:
            if (i>0):
                print(i)
                p=p+1
        print("Total Positive Numbers :: ",p) 
        input()                 
    elif (ch==2):
        print("Negative Numbers :: ")
        for i in li:
            if (i<0):
                print(i)
                n=n+1
        print("Total Negative Numbers :: ",n)
        input()
    elif (ch==3):
        print("Odd Numbers :: ")
        for i in li:
            if (i%2!=0):
                print(i)
                o=o+1
        print("Total Odd Numbers :: ",o)
        input()
    elif (ch==4):
        print("Even Numbers :: ")
        for i in li:
            if (i%2==0):
                print(i)
                e=e+1
        print("Total Even Numbers :: ",e)
        input()
    elif (ch==5):
        for i in li:
            if (i==0):
                zero=zero+1
        print("Total 0's in list :: ",zero)
        input()
    elif (ch==6):
        for i in li:
            sum=sum+i
        print("Average of  Numbers :: ",sum/n)    
        input()
    elif ch==7:
        break
    else:
        print("wrong choise")
        input()
