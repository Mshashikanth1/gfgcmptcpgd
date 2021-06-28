def linearsearch(a,e):
    for i in range(len(a)):
        if a[i]==e:
             return i

#time complextty (n)

def linearsearch_imp(a,e):
    l=0
    h=len(a)-1
    while l<=h:
        if a[l]==e:
            return l
        elif a[h]==e:
            return h
        l+=1
        h-=1



#driver code 
a=list(map(int,input().split()))
e=int(input("enter the element to be searched:"))
print("found at :",linearsearch(a,e),linearsearch_imp(a,e))

