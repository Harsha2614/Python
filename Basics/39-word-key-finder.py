n=int(input("Enter the number of words: "))
words=[]
for i in range(n):
    words.append(input())
print(words)
key=input("Enter the key: ")
found=False
for word in words:
    if key in word:
        print(word)
        found=True
        break
    else:
        print("Not Found")

        
