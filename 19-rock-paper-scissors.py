import random
list_rps=["rock","paper","scissors"]
playing=True
print("---------------------------Welcome to Rock papers Scissors------------------------")
while playing:
        user_choice=input("Enter the choice: ")
        comp_choice=random.choice(list_rps)

        if user_choice  not in list_rps:
             print("Invalid Try Again")
             continue
             
        print(f"comp_choice is {comp_choice}")
        print(user_choice)
        if(user_choice==comp_choice):
            print("Tie")
        elif(user_choice=="rock" and comp_choice=="scissors"):
            print("You win")
        elif(user_choice=="scissors" and comp_choice=="paper"):
            print("You win")
        elif(user_choice=="paper" and comp_choice=="rock"):
            print("You win")
        else:
            print("you lose")
        chose=input("Want to play again Y/N :" ).lower()
        if chose=="n":
             playing=False
print("--------------------End------------------")

    