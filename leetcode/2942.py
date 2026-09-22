class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for y in range(len(words)):
            if x in words[y]:
                res.append(y)
        return res