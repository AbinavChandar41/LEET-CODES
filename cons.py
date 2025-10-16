def cons(num):
    if not num:
        return 0
    s=set(num)
    res=0
    for nums in s:
        if nums-1 not in s:
            nex=nums+1
            while nex in s:
                nex+=1
            res=max(res,(nex-nums))
    return res
num=[1,2,5,70,3,67]
print(cons(num))