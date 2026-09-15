class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        word1 = list(word1)
        word2 = list(word2)
        while word1 or word2:
            p,p2 = '',''
            if word1:
                p = word1.pop(0)
            if word2:
                p2 = word2.pop(0)
            res += p + p2
        return res