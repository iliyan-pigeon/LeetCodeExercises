class Trie

    def __init__(self):
        self.trie = []

    def insert(self, word: str) -> None:
        self.trie.append(word)

    def search(self, word: str) -> bool:
        if word in self.trie:
            return True
        return False

    def startsWitsh(self, prefix: str) -> bool:
        for word in self.trie:
            if word.startswith(prefix):
                return True
            return False
