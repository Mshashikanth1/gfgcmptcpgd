#code
def reverse_rec(a,l,h):
    if l<h:
        a[l],a[h]=a[h],a[l]
        reverse_rec(a,l+1,h-1)
for _ in range(int(input())):
    n=int(input())
    a=[]
    for i in map(int,input().split()):
        a.append(i*i)
    reverse_rec(a,0,n-1)
    print(a)
