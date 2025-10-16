def twosum(num,k):
    l=0
    r=len(num)-1
    tot=0
    while l<r:
        tot=num[l]+num[r]
        if tot==k:
            return[num[r],num[l]]
        elif tot>k:
            r-=1
        elif tot<k:
            l+=1
    return None
num=[1,2,3,4,5,6]
k=11
print(twosum(num,k))