class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(" ")
        result = [0] * len(s)

        for ch in s:
            index = int(ch[-1]) - 1
            result[index] = ch[:-1]

        return " ".join(result)