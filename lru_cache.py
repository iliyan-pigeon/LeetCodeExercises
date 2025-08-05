class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.last_used = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.last_used.remove(key)
            self.last_used.insert(0, key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.last_used.remove(key)
        else:
            if len(self.cache) == self.capacity:
                lru = self.last_used.pop()
                del self.cache[lru]
            self.cache[key] = value

        self.last_used.insert(0, key)
        