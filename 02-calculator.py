operator=input("Enter the operator (+ - * /): ")
num1=float(input("enter num1 : "))
num2=float(input("enter num2 : "))

if operator == '+':
    print(num1+num2)
elif operator =='-':
    print(num1-num2)
elif operator=='*':
    print(num1*num2)
elif operator=='/':
    print(round(num1/num2,2))
else:
    print(f"{operator} is invalid")
