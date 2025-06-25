from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_value = 0

        for word in strs:
            if word.isnumeric():
                if int(word) > max_value:
                    max_value = int(word)

            elif len(word) > max_value:
                max_value = len(word)

        return max_value
