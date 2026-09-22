class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        d = { 
            ')':"(",
            ']':"[",
            '}':"{"
        }
        stk = []
        og = len(s)
        s = list(s)
        c = 0
        while s:
            p = s.pop(0)
            if p in d.keys():
                sp = stk.pop() if stk else None
                if sp == d[p]:
                    c += 1
                else:
                    return False
            else:
                stk.append(p)
        return c == og // 2