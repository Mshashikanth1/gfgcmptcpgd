def binarysearch(a,l,h,e):
    if e<a[0] and e>a[h]:
        return -1
    while l<=h:
        mid=l+(h-l)//2
        if e<a[mid]:
            h=mid-1
        elif a[mid]<e:
            l=mid+1
        elif a[mid]==e:
            return mid
    return -1
#calculating mid that way is very dangerous for large numbers
#instead calculate this way mid=l+(h-l)//2
def binarysearch_rec(a,l,h,e):
    if l<=h:
        mid=(l+h)//2
        if a[mid]==e:
            return mid
        elif a[mid]>e:
            return binarysearch_rec(a,l,mid-1,e)
        elif a[mid]<e:
            return binarysearch_rec(a,mid+1,h,e)
    return -1

#driver code
a=list(map(int,input().split()))
e=int(input("enter element to be searched:"))
print(binarysearch(a,0,len(a)-1,e))
print(binarysearch_rec(a,0,len(a)-1,e))
