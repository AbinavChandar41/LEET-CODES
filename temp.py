def temp(num):
    res=[0]*len(num)
    stack=[]
    for i in range(len(num)):
        while stack and num[i]>num[stack[-1]]:
            prev=stack.pop()
            res[prev]=i-prev
        stack.append(i)
    return res
num=[73,74,75,71,69,72,76,73]
print(temp(num))