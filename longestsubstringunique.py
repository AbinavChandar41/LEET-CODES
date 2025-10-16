def longestsub(num):
    s=set()
    res=0
    l=0
    for r in range(len(num)):
        while num[r] in s:
            s.remove(num[r])
            l+=1
        s.add(num[r])
        res=max(res,r-l+1)
    return res
num="abaaabcde"
print(longestsub(num))