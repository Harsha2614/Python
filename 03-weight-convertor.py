weight=float(input("Enter your Weight : "))
unit=input("Enter the Unit (kg/lb) : ")

if unit=="kg":
    weight=weight*2.205
    unit="lbs."
    print(f"Your weight is: {round(weight,2)}{unit}")
elif unit=="lb":
    weight=weight/2.205
    unit="kg"
    print(f"Your weight is: {round(weight,2)}{unit}")
else:
    print(f"{unit} is invalid")


