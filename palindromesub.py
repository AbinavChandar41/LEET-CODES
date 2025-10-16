def palin(num):
    reslen=0
    res=[-1,-1]
    for i in range(len(num)):
        r=i
        l=i
        while l>=0 and r<len(num) and num[l]==num[r]:
            if reslen<(r-l+1):
                res=l,r
                reslen=(r-l+1)
            l-=1
            r+=1
        l=i
        r=i+1
        while l>=0 and r<len(num) and num[l]==num[r]:
            if reslen<(r-l+1):
                res=l,r
                reslen=(r-l+1)
    l,r=res
    return num[l:r+1]
num="cbcg"
print(palin(num))