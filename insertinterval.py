def sub(interval, newinterval):
    res = []
    for i in range(len(interval)):
        if newinterval[1] < interval[i][0]:
            res.append(newinterval)
            return res + interval[i:]
        elif newinterval[0] > interval[i][1]:
            res.append(interval)
        else:
            newinterval = min(newinterval[0], interval[i][0]), max(newinterval[1], interval[i][1])
    res.append(newinterval)
    return res


interval = [[1, 3], [6, 9]]
newinterval = [2, 5]
print(sub(interval, newinterval))
