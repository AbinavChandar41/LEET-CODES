def para(s):
    lon = 0
    cout = 0
    for i in range(len(s)):
        r = i
        l = i
        while l >= 0 and r < len(s) and s[r] == s[l]:
            if lon < (r - l + 1):
                cout = s[l:r + 1]
                lon = (r - l + 1)
            l -= 1
            r += 1
        l = i
        r = i + 1
        while l >= 0 and r < len(s) and s[r] == s[l]:
            if lon < (r - l + 1):
                cout = s[l:r + 1]
                lon = (r - l + 1)
            l -= 1
            r += 1
    return cout


s = "cabad"
print(para(s))