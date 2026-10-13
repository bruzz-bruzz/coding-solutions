class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.append(newInterval)
        intervals.sort()
        start,end = intervals[0][0],intervals[0][1]
        l = 1
        res = []
        def lb(n,r):
            if n >= r[0] and n <= r[1]:
                return True
            return False
        while l < len(intervals):
            s,e = intervals[l][0], intervals[l][1]
            a,b = lb(s,[start,end]), lb(e,[start,end])
            if a and b:
                pass
            elif not a and not b:
                res.append([start,end])
                start = s
                end = e
            elif a and not b:
                end = e
            elif not a and b:
                res.append([start,end])
                start = s
                end = e
            l += 1
        res.append([start,end])
        return res