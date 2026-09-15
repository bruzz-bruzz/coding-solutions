class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        idx = 0
        l = float('inf')
        for x in strs:
            l = min(l,len(x))
        for x in range(l):
            res += strs[0][x]
            for y in strs:
                if y[:x+1] != res:
                    return res[:len(res) - 1]
        return res