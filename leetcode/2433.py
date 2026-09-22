class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        res = [pref[0]]
        for x in range(1,len(pref)):
            res.append(pref[x-1] ^ pref[x])
        return res