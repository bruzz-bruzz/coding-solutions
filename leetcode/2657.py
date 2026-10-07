class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a,b = set(),set()
        res = []
        for x in range(len(A)):
            a.add(A[x])
            b.add(B[x])
            res.append(len(a.intersection(b)))
        return res