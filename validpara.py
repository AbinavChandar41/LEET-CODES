def validpara(s):
    d={"{":"}","[":"]","(":")"}
    stack=[]
    for i in s:
        if i in d.keys():
            stack.append(i)
        else:
            if stack==[]:
                return False
            else:
                if d[stack[-1]]==i:
                    stack.pop()
                else:
                    return False
    if stack==[]:
        return True
    else:
        return False
s="{}[]("
print(validpara(s))