class Trie:

    def __init__(self):
        self.d = []

    def insert(self, word: str) -> None:
        self.d.append(word)

    def search(self, word: str) -> bool:
        return word in self.d

    def startsWith(self, prefix: str) -> bool:
        for x in self.d:
            p = x[:len(prefix)]
            if p == prefix:
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)