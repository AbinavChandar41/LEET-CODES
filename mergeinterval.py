def intra(interval):
    ouput=[interval[0]]
    for start,end in interval[1:]:
        last=ouput[-1][1]
        if last>=start:
            ouput[-1][1]=max(last,end)
        else:
            ouput.append([start,end])
    return ouput
interval=[[1,3],[2,6],[8,10],[15,18]]
print(intra(interval))