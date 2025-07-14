from typing import List
from collections import deque
from itertools import product



# Solution 1
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        combinations = []

        if digits == "":
            return []

        def backtrack(index, path):

            if index == len(digits):
                combinations.append("".join(path))
                return

            possible_letters = mapping[digits[index]]
            for letter in possible_letters:

                path.append(letter)
                backtrack(index + 1, path)

                path.pop()

        backtrack(0, [])

        return combinations


# Solution 2
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def combine(prefix, remaining_digits):
            if not remaining_digits:
                return [prefix]

            result = []
            for letter in mapping[remaining_digits[0]]:
                result += combine(prefix + letter, remaining_digits[1:])
            return result

        return combine("", digits)


# Solution 3
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        groups = [mapping[d] for d in digits]
        return [''.join(p) for p in product(*groups)]


# Solution 4
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        queue = deque([""])
        for digit in digits:
            letters = mapping[digit]
            for _ in range(len(queue)):
                combination = queue.popleft()
                for letter in letters:
                    queue.append(combination + letter)

        return list(queue)
