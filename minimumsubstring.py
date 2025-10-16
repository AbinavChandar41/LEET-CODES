def sub(s,t):
    d={}
    for i in t:
        d[i]=d.get(i,0)+1
    l=0
    d1={}
    res=[-1,-1]
    reslen=float('infinity')
    need=len(t)
    have=0
    for ind,ch in enumerate(s):
        d1[ch]=d1.get(ch,0)+1
        if ch in d and d[ch]==d1[ch]:
            have+=1
        while need==have:
            if reslen>(ind-l+1):
                reslen=(ind-l+1)
                res=[l,ind]
            d1[s[l]]-=1
            if s[l] in d and d1[s[l]]<d[s[l]]:
                have-=1
            l+=1
    l,ind=res
    return s[l:ind+1] if reslen!=float('infinity') else ""

s="ADOBECODEBANC"
t="ABC"
print(sub(s,t))
