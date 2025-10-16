def freq(num):
    l=1
    for i in range(1,len(num)):
        if num[i]!=num[i-1]:
            num[l]=num[i]
            l+=1
    return l
num=[1,1,1,1,2,2,2,3,3,3]
print(freq(num))