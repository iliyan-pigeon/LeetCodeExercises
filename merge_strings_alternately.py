# Solution 1
class Solution(object):
    def mergeAlternately(self, word1, word2):
        combined = ""

        longest = max(len(word1), len(word2))

        for i in range(longest):
            if i < len(word1):
                combined += word1[i]
            if i < len(word2):
                combined += word2[i]

        return combined


# Solution 2
class Solution(object):
    def mergeAlternately(self, word1, word2):
        word3 = []
        n1 = len(word1)
        n2 = len(word2)

        if n1 == n2:
            for i in range(n1):
                word3.append(word1[i]+word2[i])
        elif n1 > n2:
            for i in range(n2):
                word3.append(word1[i]+word2[i])
            word3.append(word1[(i+1):])
        else:
            for i in range(n1):
                word3.append(word1[i]+word2[i])
            word3.append(word2[(i+1):])

        return "".join(word3)
