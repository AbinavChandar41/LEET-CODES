def twosum(num,k):
    d={}
    for i in range(len(num)):
        value=num[i]
        diff=k-value
        if value not in d:
            d[diff]=i
        else:
            curr=i
            prev=d[value]
    return [num[curr],num[prev]]
num=[1,2,3,4,5,6,7,8,9]
k=15
print(twosum(num,k))