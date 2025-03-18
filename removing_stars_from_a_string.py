from collections import deque


class Solution:
    def removeStars(self, s: str) -> str:
        result = deque([])
        previous_stars = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == "*":
                previous_stars += 1
                continue
            elif previous_stars > 0:
                previous_stars -= 1
                continue

            result.appendleft(s[i])

        return "".join(result)


class Solution:
    def removeStars(self, s: str) -> str:
        letters = []
        for letter in s:
            if letter == "*":
                letters.pop()
            else:
                letters.append(letter)

        return "".join(letters)
