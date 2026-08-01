#used if __name__=='__main__'

print("----------Banking Program------------------")
def showbalance(balance):
    print("--------------------------------------------")
    print(f" Current Balance is ${balance:.2f}")

def deposit(balance):
    print("--------------------------------------------")
    dep=float(input("Enter the amount to be deposited: "))
    if dep<0:
        print("Enter Valid amount to be deposited!!")
        return 0
    else:
        return dep

def withdraw(balance):
    print("--------------------------------------------")
    withd=float(input("Enter the amount to be Withdrwan: "))
    if withd>balance:
        print("Incuffient funds !!")
        return 0
    else: 
        return withd



def main():
        balance=0
        is_running=True

        while is_running:
            print("--------------------------------------------")
            print("1.Show Balance")
            print("2.Deposit amount")
            print("3.Withdraw amount")
            print("4.Exit")
            print("--------------------------------------------")

            choice=input("Enter the choice(1-4): ")

            match choice:
                case '1':
                    showbalance(balance)
                case '2':
                    
                    balance+=deposit(balance)
                    showbalance(balance)
                case '3':
                
                    balance-=withdraw(balance)
                case '4':
                    is_running=False
                case _:
                    print("Invalid try again")
        print("Have a nice day!!!")

if __name__=='__main__':
    main()
# Importing a file runs it

# if __name__ == "__main__": prevents accidental execution

# It’s essential once you move beyond single-file scripts

#“This is the main guard. It ensures that code runs only when the file is executed directly and not when it is imported as a module.”