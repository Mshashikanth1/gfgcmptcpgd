def sumofarray(arr,l,h):
    sum1=0
    while l<h:
          sum1+=arr[l]+arr[h]
          l+=1
          h-=1
    if len(a)%2==0:
        return sum1
    else:
        return sum1+arr[l]
a=list(map(int,input().split()))
print(sumofarray(a,0,len(a)-1))
print(sum(a))

