class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        def recur(s,n):
            if len(s) >= n:
                res.append(s)
            else:
                if s[len(s) - 1] == '0':
                    recur(s + '1',n)
                else:
                    recur(s + '1',n)
                    recur(s + '0',n)
        recur('0',n)
        recur('1',n)
        return res