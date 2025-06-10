from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []

        words = set(words)

        for word in words:
            for second_word in words:
                if word in second_word and word not in result:
                    result.append(word)

        return result
