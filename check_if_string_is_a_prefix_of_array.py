from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        concat_words = ""

        for word in words:
            concat_words += word

            if concat_words == s:
                return True

        return False
