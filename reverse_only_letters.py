class Solution:
    def reserveOnlyLetters(self, s: str) -> str:
        characters = []
        symbol_indexes = {}

        result = ""

        for i, v in enumerate(s):
            if not v.isalpha():
                symbol_indexes[i] = v
            else:
                characters.append(v)

        counter = 0

        while characters or symbol_indexes:
            if counter in symbol_indexes:
                result += symbol_indexes[counter]
                del symbol_indexes[counter]
            else:
                result += characters.pop()

            counter += 1

        return result
