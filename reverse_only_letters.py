class Solution:
    def reserveOnlyLetters(self, s: str) -> str:
        characters = []
        dash_indexes = []

        result = ""

        for i, v in enumerate(s):
            if v == "-":
                dash_indexes.append(i)
            else:
                characters.append(v)

        counter = 0

        while characters:
            if counter in dash_indexes:
                result += "-"
            else:
                result += characters.pop()

            counter += 1

        return result
