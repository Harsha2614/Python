numbers = [5,4,3,2,1]
n=len(numbers)
for i in range(n-1):
    mini=i
    for j in range(i+1,n):
        if numbers[j]<numbers[mini]:
            mini=j
    numbers[i],numbers[mini]=numbers[mini],numbers[i]
print(numbers)
