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
