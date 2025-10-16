def inter(interval):
    start = sorted([i[0] for i in interval])
    end = sorted([i[1] for i in interval])

    s = 0
    e = 0
    count = 0
    res = 0
    while s < len(interval):
        if start[s] < end[e]:
            count += 1
            res = max(res, count)
            s += 1
        else:
            count -= 1
            e += 1
    return res


interval = [[0, 30], [5, 10], [15, 20]]
print(inter(interval))
