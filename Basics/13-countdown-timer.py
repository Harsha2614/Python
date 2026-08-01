import time

t=int(input("Enter time in seconds : "))

for i in range(t,0,-1): #or 
    seconds=i%60
    min=int(i/60)%60
    hr=int(i/3600)

    print(f'{hr:02}:{min:02}:{seconds:02}')
    time.sleep(1)

print("Time is up !")