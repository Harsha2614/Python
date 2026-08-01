#optimized bubble sort best case O(n)
numbers = [5,4,3,2,1]

n=len(numbers)

for pass_number in range(n-1):

    swapped =False

    for i in range(n-1-pass_number):
      
      if numbers[i]>numbers[i+1]:
         
         numbers[i],numbers[i+1]=numbers[i+1],numbers[i]

         swapped=True

    if not swapped:

        break

print(numbers)
