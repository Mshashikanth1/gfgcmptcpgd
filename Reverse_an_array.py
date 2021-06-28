#time complexity is O(n)

def reverse(arr,l,h):
    while l<h:
        arr[l],arr[h]=arr[h],arr[l]
        l+=1
        h-=1

def reverse_rec(arr,l,h):
    if l<h:
        arr[l],arr[h]=arr[h],arr[l]
        reverse_rec(arr,l+1,h-1)

def reverse_slicepy(arr):
    return arr[::-1]

arr=list(map(int,input().split()))
reverse(arr,0,len(arr)-1)
print(arr)
reverse_rec(arr,0,len(arr)-1)
print(arr)
arr=reverse_slicepy(arr)
print(arr)

#one can also reverse the list by slising method

