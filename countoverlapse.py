def intra(interval):
    prev = interval[0][1]
    ret = 0
    for start, end in interval[1:]:
        if prev <= start:
            prev = end
        else:
            ret += 1
            prev = min(end, prev)
    return ret


interval = [[1, 2], [2, 3], [3, 4], [1, 3], [1, 9]]
print(intra(interval))

