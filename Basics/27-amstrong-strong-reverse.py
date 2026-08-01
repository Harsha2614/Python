import math
digit=int(input("Enter number: "))

#Strong Number
def strong():
        temp=digit
        total=0
        while temp>0:
            eachdigit=temp%10
            fact=math.factorial(eachdigit)
            total+=fact
            temp=temp//10

        print(digit)
        print(total)

        if(total==digit):
            print(f"{digit} is a Strong number")
        else:
            print(f"{digit} is not a Strong number")

#Amstrong Number

def Amstrong():
    temp=digit
    total=0
    while temp>0:
        lastdigit=temp%10
        power=math.pow(lastdigit,len(str(digit)))
        total+=power
        temp=temp//10

    if total==digit:
        print(f"{digit} is an Amstrong number")
    else:
        print(f"{digit} is not an Amstrong number")

#reversed number
def reverse():
    temp=digit
    reverse=0

    while temp>0:
        lastval=temp%10
        reverse=reverse*10+lastval
        temp//=10

    print(f"reversed value of {digit} is {reverse}")


strong()
Amstrong()
reverse()