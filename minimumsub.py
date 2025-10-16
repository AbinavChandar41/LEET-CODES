def hard(s,t):
    d={}
    a={}
    for ind,ch in enumerate(t):
        d[ch]=d.get(ch,0)+1
    need=len(d)
    have=0
    res=[-1,-1]
    l=0
    reslen=float('infinity')
    for ind,ch in enumerate(s):
        a[ch]=a.get(ch,0)+1
        if ch in d and d[ch]==a[ch]:
            have+=1
        while have==need:
            if reslen>(ind-l+1):
                res=[l,ind]
                reslen=(ind-l+1)
            a[s[l]]-=1
            if s[l] in d and d[s[l]]>a[s[l]]:
                have-=1
            l+=1
    l,ind=res
    return s[l:ind+1] if reslen!=float('infinity') else ""
s="ADOBECODEBANC"
t="ABC"
print(hard(s,t))