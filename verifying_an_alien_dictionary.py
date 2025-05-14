from typing import List


# Solution 1
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_index_map = {char: index for index, char in enumerate(order)}

        def alien_order(word):
            return [char_index_map[char] for char in word]

        sorted_words = sorted(words, key=alien_order)

        return words == sorted_words


# Solution 2
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        d = {}
        for i in range(len(order)):
            d[order[i]] = i + 1

        for i in range(len(words) -1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False
                if words[i][j] != words[i+1][j]:
                    if d[words[i][j]] > d[words[i+1][j]]:
                        return False
                    break
        return True
