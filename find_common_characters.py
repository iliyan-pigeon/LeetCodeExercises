from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        chars_map = {}

        for ch in words[0]:
            if ch not in chars_map:
                chars_map[ch] = 0
            chars_map[ch] += 1

        keys_to_remove = []

        for i in range(1, len(words)):

            for ch in chars_map.keys():
                if ch not in words[i]:
                    keys_to_remove.append(ch)

                elif chars_map[ch] > words[i].count(ch):
                    chars_map[ch] = words[i].count(ch)

        for key in keys_to_remove:
            chars_map.pop(key)

        for k, v in chars_map.items():
            for _ in range(v):
                result.append(k)

        return result
      
