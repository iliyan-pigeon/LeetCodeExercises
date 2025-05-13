from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        result = []
        first_index = 0
        last_index = len(s)

        for i in range(len(s)):
            if s[i] == "I":
                result.append(first_index)
                first_index += 1

                if i == len(s)-1:
                    result.append(last_index)

            elif s[i] == "D":
                result.append(last_index)
                last_index -= 1

                if i == len(s)-1:
                    result.append(first_index)

        return result
      
