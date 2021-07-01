#code
def f(n):                #this programme will find the anser of performing f(f(f(......f(N)...ktimes on any int n
    return n^(n%10)
for _ in range(int(input())):
    n,k=map(int,input().split())
    for i in range(k):
        n=f(n)
        if n%10==0:
            break
    print(n)
