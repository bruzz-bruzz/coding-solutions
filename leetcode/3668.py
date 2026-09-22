class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        res = [0] * len(friends)
        d = {}
        o = 0
        for x in range(len(order)):
            if order[x] in friends:
                d[order[x]] = o
                o += 1
        for x in d.keys():
            res[d[x]] = x
        return res