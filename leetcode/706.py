class MyHashMap:

    def __init__(self):
        self.k = []
        self.v = []

    def put(self, key: int, value: int) -> None:
        if key not in self.k:
            self.k.append(key)
            self.v.append(value)
        else:
            i = self.k.index(key)
            self.v[i] = value
    def get(self, key: int) -> int:
        if key in self.k:
            i = self.k.index(key)
            return self.v[i]
        return -1

    def remove(self, key: int) -> None:
        if key in self.k:
            i = self.k.index(key)
            self.k.pop(i)
            self.v.pop(i)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)