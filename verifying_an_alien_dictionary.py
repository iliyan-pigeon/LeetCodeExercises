from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_index_map = {char: index for index, char in enumerate(order)}

        def alien_order(word):
            return [char_index_map[char] for char in word]

        sorted_words = sorted(words, key=alien_order)

        return words == sorted_words
      
