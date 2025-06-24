from typing import List


class Solution:
    def oddString(self, words: List[str]) -> str:

        converted = {}

        for word in words:
            current = []
            for i in range(len(word)-1):
                current.append([(ord(word[i+1]) - 97) - (ord(word[i]) - 97), (ord(word[2]) - 97) - (ord(word[1]) - 97)])

            current = str(current)
            if current not in converted:
                converted[current] = []
            converted[current].append(word)

        for v in converted.values():
            if len(v) == 1:
                return v[0]
