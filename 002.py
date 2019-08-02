class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.lru = []

    def get(self, key: int) -> int:
        if key in self.map:

            self.lru.remove(key)
            self.lru.append(key)
            return self.map[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.map) == self.cap:
            del self.map[self.lru[0]]
            del self.lru[0]

        if key in self.map:
            self.lru.remove(key)

        self.map[key] = value
        self.lru.append(key)


obj = LRUCache(10)
lst = [[2], [2, 6], [1], [1, 5], [1, 2], [1], [2]]
for i in lst:
    if len(i) == 1:
        rst = obj.get(i[0])
        print(rst)
    else:
        obj.put(i[0], i[1])
