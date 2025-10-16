def containing(num):
    l=0
    r=len(num)-1
    res=0
    while l<r:
        diff=r-l
        m=min(num[l],num[r])
        f=diff*m
        if res<f:
            res=f
        elif num[l]<num[r]:
            l+=1
        else:
            r-=1
    return res
num=[1,8,6,2,5,4,8,3,7]
print(containing(num))