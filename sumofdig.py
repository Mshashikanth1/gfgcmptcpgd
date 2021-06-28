def sumofdig(n):
    sum1=0
    while n:
        dig=n%10
        sum1+=dig
        n=n//10
    return sum1

def sumofdig_rec(n):
    if n==0:
        return 0
    else:
        return (n%10) +sumofdig_rec(n//10)

def sumofdig_str(n):
    sum1=0
    for i in n:
        sum1+=int(i)
    return sum1

def sumofdig_tailrec(n,v):
    if n<10:
        v+=n
        return v
    return sumofdig_tailrec(n//10,(n%10)+v)


#driver code
n=input()
print(sumofdig(int(n)))
print(sumofdig_rec(int(n)))
print(sumofdig_str(n))
print(sumofdig_tailrec(int(n),0))
