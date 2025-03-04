# Solution 1
def reverseVowels(s: str) -> str:
    vowels_list = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    current_vowels = []
    for i in range(len(s)):
        if s[i] in vowels_list:
            current_vowels.append(s[i])

    for i in range(len(s)):
        if s[i] in vowels_list:
            s = s[:i] + current_vowels.pop() + s[i+1:]
    return s


# Solution 2
VOWELS = set("aeiouAEIOU")


class Solution:
    def reverseVowels(self, s: str) -> str:
        begin = 0
        end = len(s) - 1
        sl = list(s)
        while begin < end:
            while (s[begin] not in VOWELS) and (begin < end):
                begin += 1

            while (s[end] not in VOWELS) and (begin < end):
                end -= 1

            if begin != end:
                sl[begin], sl[end] = sl[end], sl[begin]

            begin += 1
            end -= 1
        return ''.join(sl)
