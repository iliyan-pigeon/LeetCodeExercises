from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:

        the_plate = ""

        for word in words:
            for ch in licensePlate:
                if ch.isalpha() and ch.lower() not in word.lower():
                    continue

                if len(the_plate) > len(word) or not the_plate:
                    the_plate = word

        return the_plate
      
