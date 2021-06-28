def palindrome(st,l,h):
    while l<h:
        if st[l]!=st[h]:
            return False
        l+=1
        h-=1
    return True

def palindrome_rec(st,l,h):
    if l<h:
        if st[l]!=st[h]:
            return False
        else:
            return palindrome_rec(st,l+1,h-1)
    return True


def palindrome_str(st):
    return st==st[::-1]

def palindrome_join(st):
    rev=''.join(reversed(st))
    return st==rev

def palindrome_one_extra_var(st):
    w=""
    for i in st:
        w=i+w
    return st==w

def palindrome_flag(st):
    flag=0
    j=-1
    for i in st:
        if i !=st[j]:
            j-=1
            flag=1
            break
        j-=1
    return flag==0

#dirver code
st=input()
print(palindrome(st,0,len(st)-1))
print(palindrome_rec(st,0,len(st)-1))
print(palindrome_str(st))
print(palindrome_join(st))
print(palindrome_one_extra_var(st))
print(palindrome_flag(st))
