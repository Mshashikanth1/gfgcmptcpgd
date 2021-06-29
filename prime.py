import math
def prime_sch(n):  #school method
    for i in range(2,n):
        if n%i==0:
            return False
    return True

#since every prime can be expressed as 6*k+i for some k,i we  can first chek #for 2 and 3 and gor futther
#also it is enough to chek for sqrt(n) integers because largefacters are also# factors of small
#so more efficieat implementation will be like

def prime_eff(n):
    if n%2==0 or n%3==0:
        return False
    for i in range(4,math.ceil(math.sqrt(n))):
        if n%i==0:
            return False
    return True

#driver code
n=int(input("is this prime ? ,"))
print(prime_sch(n))
print(prime_eff(n))
