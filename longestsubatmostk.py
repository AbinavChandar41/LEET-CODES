def sub(num,k):
    tot=0
    l=0
    d={}
    res=""
    for ind,ch in enumerate(num):
        d[ch]=d.get(ch,0)+1
        while len(d)>k:
            d[num[l]]-=1
            if d[num[l]]==0:
                del d[num[l]]
            l+=1
        tot=max(tot,(ind-l+1))
        res=num[l:ind+1]
    return tot,res
num="cccdcccc"
k=2
print(sub(num,k))