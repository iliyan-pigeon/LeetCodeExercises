from typing import List
from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:

        filtered_plate = "".join([i for i in licensePlate if i.isalpha()]).lower()
        plate_count = Counter(filtered_plate)

        shortest_word = None

        for word in words:
            word_count = Counter(word.lower())

            if all(word_count[ch] >= plate_count[ch] for ch in plate_count):

                if shortest_word is None or len(word) < len(shortest_word):
                    shortest_word = word

        return shortest_word
        
