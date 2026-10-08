class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        c = 0
        for x in sentences:
            c = max(c, len(x.split(" ")))
        return c