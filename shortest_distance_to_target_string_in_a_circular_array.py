from typing import List


# Solution 1
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        shortest_path = 0

        pointer_left = startIndex
        pointer_right = startIndex

        left_finished = False
        right_finished = False

        while not left_finished and not right_finished:
            if words[pointer_left] == target or words[pointer_right] == target:
                return shortest_path

            pointer_left -= 1
            pointer_right += 1
            shortest_path += 1

            if pointer_left == -1:
                pointer_left = len(words)-1

            if pointer_right == len(words):
                pointer_right = 0

            if pointer_left == startIndex:
                left_finished = True
            if pointer_right == startIndex:
                right_finished = True

        return -1


# Solution 2
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        ans = float('inf')
        n = len(words)

        for i, word in enumerate(words):
            if word == target:
                ans = min(ans, abs(startIndex - i), n - abs(startIndex - i))

        return ans if ans != float('inf') else -1
