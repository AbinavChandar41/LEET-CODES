def threesum(num,k):
    if len(num)<3:
        return 0
    res=[]
    tot=0
    num.sort()
    for i in range(len(num)):
        if num[i]==num[i-1] and i>0:
            continue
        r=len(num)-1
        l=i+1
        while l<r:
            tot=num[r]+num[l]+num[i]
            if tot==k:
                res.append([num[r],num[l],num[i]])
                l+=1
                r-=1
                while num[l]==num[l-1] and l<r:
                    l+=1
                while num[r]==num[r+1] and l<r1:
                    r-=1
            elif tot>k:
                r-=1
                while num[r]==num[r-1] and l<r:
                    r-=1
            elif tot<k:
                l+=1
                while num[l]==num[l-1] and l<r:
                    l+=1
    return res
num=[-1,0,1,2,-1,-4]
k=0
print(threesum(num,k))