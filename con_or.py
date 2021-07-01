def game_with_number (arr,  n) :  #this function will print the bit wise or ofconsicutive  elements in a given array
    a=[]
    for i in range(n-1):
        a.append(arr[i]|arr[i+1])
    if len(a)==n:
        return a
    else:
        a.append(arr[-1])
        return a
        
 #driver code
 n=int(input())
 arr=list(map(int,input().split()))
 ans=game_with_numver(arr,n)
 print(*ans)
