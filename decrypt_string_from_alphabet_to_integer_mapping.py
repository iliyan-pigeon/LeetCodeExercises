class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabet = "abcdefjhijklmnopqretuvwxyz"
        result = ""

        skip = 0

        for i in range(len(s)-1, -1, -1):

            if skip > 0:
                skip -= 1
                continue

            if s[i] == "#":
                result = alphabet[int(s[i-2:i])] + result
                skip = 2
            else:
                result = alphabet[int(s[i])] + result

        return result
