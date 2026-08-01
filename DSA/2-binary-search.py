target=int(input("Enter the target to be found :[10,20,30,40,50,60,70] "))
numbers = [10,20,30,40,50,60,70]
found=False
low=0
high=len(numbers)-1
while low<=high:
    mid=(low+high)//2
    if(target==numbers[mid]):
        print(f"found at {mid}")
        found=True
        break
    elif(target<numbers[mid]):
        high=mid-1
    else:
        low=mid+1
        
if not found:
        print("Element not found")
        