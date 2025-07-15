class Solution:
    def numDecodings(self, s: str) -> int:
        combinations = []
        ascii_base = 64

        for i in range(len(s)):
            if chr(int(s[i])+ascii_base).isalpha():
                combinations.append(s[i])
            if chr(int(s[i:i+2])+ascii_base).isalpha():
                combinations.append(int(s[i:i+2]))

        return len(combinations) // 2
