p=0
r=0
t=0

while p<=0:
    p=float(input("enter the principle amount : "))
    if p<=0:
     print(f'p cannot be less than or equal to zero')

while r<=0:
    r=float(input("enter the rate : "))
    if r<=0:
     print(f'r cannot be less than or equal to zero')

while t<=0:
    t=int(input("enter time in years : "))
    if t<=0:
     print(f't cannot be less than or equal to zero')

amount=p*((1+(r/100)))**t
print(f'Balance after {t} years will be {amount}')

    