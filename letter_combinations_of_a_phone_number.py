class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        combinations = []

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
