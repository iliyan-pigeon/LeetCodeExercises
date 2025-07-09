# Solution 1
class Solution:
    def reverseDegree(self, s: str) -> int:
        degrees = []
        alphabet = {'a': 26, 'b': 25, 'c': 24, 'd': 23, 'e': 22, 'f': 21, 'g': 20, 'h': 19, 'i': 18, 'j': 17,
                    'k': 16, 'l': 15, 'm': 14, 'n': 13, 'o': 12, 'p': 11, 'q': 10, 'r': 9, 's': 8, 't': 7, 'u': 6,
                    'v': 5, 'w': 4, 'x': 3, 'y': 2, 'z': 1}

        for i, ch in enumerate(s):
            degree = alphabet[ch] * (i+1)
            degrees.append(degree)

        return sum(degrees)


# Solution 2
class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            x = ord(s[i])
            x = abs(x-122) + 1
            ans += (x * (i+1))
        return ans
