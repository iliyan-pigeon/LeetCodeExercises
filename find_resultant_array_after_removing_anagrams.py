from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        anagrams = True

        while anagrams:
            for i in range(1, len(words)):
                if sorted(words[i]) == sorted(words[i-1]):
                    words.pop(i)
                    break
            else:
                anagrams = False

        return words
