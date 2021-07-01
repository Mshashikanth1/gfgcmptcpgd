def findsetbits(n):
    c=0
    while n!=0:
        c+=n&1
        n>>=1
    return c
n=int(input())
print(findsetbits(n))
