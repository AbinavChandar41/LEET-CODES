def histo(num):
    res=0
    stack=[]
    for ind,h in enumerate(num):
        start=ind
        while stack and h<stack[-1][1]:
            index,height=stack.pop()
            res=max(res,height*(ind-index))
            start=ind
        stack.append([start,h])
    for i,(start,height) in enumerate(stack):
        res=max(res,height*(len(num)-start))
    return res
num=[2,1,5,6,2,3]
print(histo(num))