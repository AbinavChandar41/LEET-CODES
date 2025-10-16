def kelements(num,k):
    d={}
    for i in num:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    n=len(num)
    res=[0]*(n+1)
    for num,freq in d.items():
        if res[freq]==0:
            res[freq]=[num]
        else:
            res[freq].append(num)
    ret=[]
    for i in range(n,-1,-1):
        if res[i]!=0:
            ret.extend(res[i])
        if len(res)==k:
            break
    return ret[:k]
num=[1,2,3,4,1,2,6,7,9]
k=2
print(kelements(num,k))