from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph_list = [i.strip(",.!?';:").lower() for i in paragraph.replace(",", " ").split()]
        occurrences = {}
        result = ""
        highest_amount = 0

        for word in paragraph_list:
            if word not in banned:
                if word not in occurrences:
                    occurrences[word] = 0
                occurrences[word] += 1
                if occurrences[word] > highest_amount:
                    highest_amount = occurrences[word]
                    result = word

        return result