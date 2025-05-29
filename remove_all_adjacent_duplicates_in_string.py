from collections import Counter


class Solution:
    def removeDuplicates(self, s: str) -> str:
        amounts = Counter(s)

        for ch, count in amounts.items():
            if count % 2 != 0 and count != 1:
                s = s.replace(ch, "", count-1)
            elif count % 2 == 0:
                s = s.replace(ch, "", count)

        return s
