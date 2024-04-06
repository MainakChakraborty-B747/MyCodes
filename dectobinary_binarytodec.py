import time
import os
import sys
def decimaltobinary():
    data=int(input("Enter a number: "))
    result=[]
    s=""
    while(data>0):
        r=data%2
        result.append(str(int(r)))
        data=(data-r)/2
    for i in range(0,len(result)):
        s=s+result[i]
    print(f"binary equivalent is: {s[::-1]}")#using reverse slicing
    time.sleep(5)
    d=input("Convert more decimal to binary ? (y/n): ")
    if d=='y' or d=="Y":
        os.system('cls')
        decimaltobinary()
    else:
        print("Returning to home....")
        main()


def binarytodecimal():
    data=input("Enter a number: ")
    result=[]
    temp=data[::-1]
    l=len(data)
    for i in range(0,l):
        s=int(temp[i])*(2**i)
        result.append(str(s))
    f=0
    for i in range(0,l):
        f=f+int(result[i])
    print(f"Decimal Equivalent is: {f}")
    time.sleep(5)
    d=input("Convert more binary to decimal ? (y/n): ")
    if d=='y' or d=="Y":
        os.system('cls')
        binarytodecimal()
    else:
        print("Returning to home....")
        main()


def main():
    print("This program Converts Decimal to Binary and vice versa.........")
    print("1.Decimal to Binary   2.Binary to Decimal")
    c=int(input("Choose your preference: "))
    if c==1:
        print("Convert decimal to binary")
        decimaltobinary()
    elif c==2:
        print("Convert binary to decimal")
        binarytodecimal()
    else:
        print("Wrong Choice, terminating..")
        sys.exit()

main()
