foods=[]
prices=[]
total=0

while True:
    food=input("Enter a food to add (q to Quit) : ")
    if food.lower()=='q':
        break
    else:
        price=float(input("Enter the price : "))
        foods.append(food)
        prices.append(price)
print()
print('-------------Cart Quantity-------------------')
for i in range(len(foods)):
    print(foods[i], prices[i])


for p in prices:
    total+=p
print()
print("Total bill",total) 
