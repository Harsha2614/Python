n=int(input("Enter the number: "))
arr=list(map(int,input().split()))
freq={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
for key, value in freq.items():
    print(key, value)