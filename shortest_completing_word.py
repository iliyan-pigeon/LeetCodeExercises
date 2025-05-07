from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:

        filtered_plate = "".join([i for i in licensePlate if i.isalpha()]).lower()

        the_plate = ""

        for word in words:
            valid = True
            for ch in filtered_plate:
                if filtered_plate.count(ch) != word.lower().count(ch):
                    valid = False
                    break

            if valid and len(the_plate) > len(word) or valid and len(the_plate) == 0:
                the_plate = word

        return the_plate
        
