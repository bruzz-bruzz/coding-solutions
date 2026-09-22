class Solution:
    def interpret(self, command: str) -> str:
        res = ''
        d = {
            'G':"G",
            '()':'o',
            '(al)':"al"
        }
        l = 0
        w = ''
        while l < len(command):
            w += command[l]
            if w in d.keys():
                res += d[w]
                w = ''
            l += 1
        if w in d.keys():
            res += d[l]
        return res