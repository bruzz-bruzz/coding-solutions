class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = 0
        for x in words:
            f = False
            for y in x:
                if y not in allowed:
                    f = True
                    break
            c += 1 if not f else 0
        return c