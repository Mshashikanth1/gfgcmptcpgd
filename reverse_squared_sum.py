#code
def reverse_rec(a,l,h):
    while l<h:
        a[l],a[h]=a[h],a[l]
        l+=1
        h-=1
        
for _ in range(int(input())):
    n=int(input())
    a=[]
    sig=1
    for i in map(int,input().split()):
        a.append(i*i)
    reverse_rec(a,0,n-1)
    sum1=0
    for i in a:
        if sig==1:
          sum1+=i
          sig=0
        else:
            sum1-=i
            sig=1
    print(sum1)
