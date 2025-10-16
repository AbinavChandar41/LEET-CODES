def anagram(s):
    d={}
    for i in s:
        t="".join(sorted(i))
        if t not in d:
            d[t]=[i]
        else:
            d[t].append(i)
    return list(d.values())
s=["eat","tea","tan","ate","nat","bat"]
print(anagram(s))