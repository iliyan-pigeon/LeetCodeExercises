class MyHashSet:

    def __init__(self):
        self.hashset = []

    def add(self, key: int) -> None:
        self.hashset.append(key)

    def remove(self, key: int) -> None:
        self.hashset.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.hashset:
            return True
        return False
      
