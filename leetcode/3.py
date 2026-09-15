def lengthOfLongestSubstring(s: str) -> int:
    if not res:
        return 0
    res = 1
    l,r = 0,1
    st = s[l]
    sett = set()
    sett.add(s[l])
    while r < len(s):
        while s[r] in sett:
            if st[l] in sett:
                sett.remove(st[l])
            l += 1
        st += s[r]
        sett.add(s[r])
        r += 1
        res = max(res,r-l)
    return res
s = "1R1T7"
print(lengthOfLongestSubstring(s))