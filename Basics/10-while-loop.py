# name=input('Enter your name: ')
# while name == "":
#     print("invalid name try again")
#     name=input("Enter your name : ")
# print(f"Hello! {name}")

# food=input("Enter your favorite food (q to quit): ")
# while not food=="q":
#     print(f"your fav food is {food}")
#     food=input("Enter  your another favorite food : ")
# print('bye')


num=int(input('Enter the number between 1-10 '))
while num<1 or num>10:
    print(f'{num} is out of  range')
    num=int(input('Enter the number between 1-10 '))
print(f'Your number is {num}')
    