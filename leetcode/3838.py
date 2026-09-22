class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ''
        for x in words:
            c = 0
            for y in x:
                c += weights[ord(y) - 97]
            res += chr(122 - (c % 26))
        return res