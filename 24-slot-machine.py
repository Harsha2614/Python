import random
print('---------------Welcome to the slot Machine-----------------------')
def showsymbols():
    symbols=['❤️','😁','😂','😎','😉']
    return [random.choice(symbols) for _ in range(3)]
    pass
def printsymbols(result):
        print('-------------------')
        print('  |  '.join(result))
        print('-------------------')


    
def finalamount(result,bet):
    if result[0]==result[1]==result[2]:
         if result[0]=='😁':
              return bet*2
         elif result[0]=='😂':
              return bet*3
         elif result[0]=='😉':
              return bet*5
         elif result[0]=='😎':
              return bet*10
         elif result[0]=='❤️':
              return bet*20
         
    return 0

def main():
        balance=100
        while balance>0:
            print("------------------------------------")
            print(f"current balance: {balance}")
            print("------------------------------------")
            bet=input("Enter the bet: ")
            if not bet.isdigit():
                print("Invalid input Try agin")
                continue
            bet=int(bet)
            if bet>balance:
                print("insufficient funds")
                continue
            if bet<=0:
                print("bet amount should be greater than 0")
                continue
            
            balance-=bet
            
            result=showsymbols()
            printsymbols(result)
            payout=finalamount(result,bet)
            if payout>0:
                print(f"You won: {payout}")
                
            else:
                print("You did not win")
                
            balance+=payout
            print(f"Current amount {balance}")
            print("------------------------------------")
            play=input("Do you want to continue (Y/N):").upper()
            if play !='Y':
                break
        print("------------------------------------")
        print(f"Final amount:{balance}")
        print('Thank you for playing')
        print('------------------------XXXXXXXXXXXXXXXXXXXXXXXXXX------------------------------------')

if __name__=='__main__':
     main()




