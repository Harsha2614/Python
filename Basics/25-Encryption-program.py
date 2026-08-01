import random
import string

# Step 1: Create character set
chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)

# Step 2: Create key mapping
keys = chars.copy()
random.shuffle(keys)

# Step 3: Encryption
original = input("Enter the message to be encrypted: ")
cipher = ""

for ch in original:
    index = chars.index(ch)
    cipher += keys[index]

print(f"Encrypted Text: {cipher}")

# Step 4: Decryption
decrypt = input("Enter the message to be decrypted: ")
decrypted = ""

for ch in decrypt:
    index = keys.index(ch)
    decrypted += chars[index]

print(f"Decrypted Text: {decrypted}")