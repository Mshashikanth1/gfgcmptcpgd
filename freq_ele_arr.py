def freq_ele_arr(a,l,h):
    v=[0]*(h+1)
    for i in range(l,h+1):
        c=1
        if v[i]==1:
            continue
        for j in range(i+1,h+1):
            if a[i]==a[j]:
                v[j]=1
                c+=1
        print(a[i],c)
#int the above function we use two loops one for selecting an element and 
#another for counting the number of times the element repeted
#to overcome the selection of ele already counted and repeated we use a 
#an array visited for marking ele visited we do not enter the second loop

#time complexity 0(n^2)

#the efficant way is to use a hash map

def fre_ele_arr_hash(a,l,h):
    d={}
    for i in a:
        if i not in d.keys():
            d[i]=1
        else:
            d[i]+=1
    print(d,end="\n")



#driver code
a=list(map(int,input().split()))
freq_ele_arr(a,0,len(a)-1)
fre_ele_arr_hash(a,0,len(a)-1)
