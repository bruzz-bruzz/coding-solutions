class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        while n > 1:
            print(res)
            s = ''
            c = 0
            l = 0
            prev = res[l]
            while l < len(res):
                if res[l] != prev:
                    s += str(c) + prev
                    c = 1
                else:
                    c += 1
                prev = res[l]
                l += 1
            if c > 0:
                s += str(c) + prev
            res = s
            n -= 1
        return res