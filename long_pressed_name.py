from collections import Counter


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name = Counter(name)
        typed = Counter(typed)

        for ch, count in name.items():
            if ch not in typed:
                return False
            elif typed[ch] < count:
                return False

        return True
