class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result = []
        current = [words[0]]

        for i in range(1, len(groups)):
            if groups[i-1] == groups[i]:
                if len(current) > len(result):
                    result = current
                    current = [words[i]]
            else:
                current.append(words[i])

        if len(current) > len(result):
            result = current

        return result
