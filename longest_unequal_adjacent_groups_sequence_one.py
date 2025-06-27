from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result = [words[0]]
        last_element_added = groups[0]

        for i in range(1, len(groups)):
            if last_element_added != groups[i]:
                result.append(words[i])
                last_element_added = groups[i]

        return result
