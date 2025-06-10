class Solution:
    def reformat(self, s: str) -> str:
        digits = ""
        letters = ""
        result = ""

        for ch in s:
            if ch.isalpha():
                letters += ch
            else:
                digits += ch

        if abs(len(letters) - len(digits)) > 1:
            return result

        result = ["."] * (len(letters) + len(digits))

        index = 0
        if len(letters) >= len(digits):
            for i in range(1, len(result), 2):
                result[i] = digits[index]
                index += 1
                if index == len(digits):
                    break

            index = 0
            for i in range(len(result)):
                if result[i] == ".":
                    result[i] = letters[index]
                    index += 1
        else:
            index = 0
            for i in range(1, len(result), 2):
                result[i] = letters[index]
                index += 1
                if index == len(digits):
                    break

            index = 0
            for i in range(len(result)):
                if result[i] == ".":
                    result[i] = digits[index]
                    index += 1

        return "".join(result)
