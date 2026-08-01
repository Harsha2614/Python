def simplecipher(encrypted,k):
    result=[]
    k=k%26
    for ch in encrypted:
        init=ord(ch)-ord('A')
        finalval=(init-k)%26
        result.append(chr(finalval+ord('A')))
    return ''.join(result)

print(simplecipher('VTAOG',2))



