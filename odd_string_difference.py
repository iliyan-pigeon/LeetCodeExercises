from typing import List


class Solution:
    def oddString(self, words: List[str]) -> str:

        converted = {}

        for word in words:
            current = str([(ord(word[1])-97)-(ord(word[0])-97), (ord(word[2])-97)-(ord(word[1])-97)])
            if current not in converted:
                converted[current] = []
            converted[current].append(word)

        for v in converted.values():
            if len(v) == 1:
                return v[0]
