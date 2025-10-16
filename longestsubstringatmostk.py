def sub(s,k):
    l=0
    res=0
    d={}
    for ind,ch in enumerate(s):
        d[ch]=d.get(ch,0)+1
        while len(d)>k:
            d[s[l]]-=1
            if d[s[l]]==0:
                d.pop(s[l])
            l+=1
        res=max(res,ind-l+1)
    return res
s="abc"
k=2
print(sub(s,k))