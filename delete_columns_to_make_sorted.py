from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        pointer = 0

        while pointer < len(strs[0]):
            previous = None
            for word in strs:
                if previous is None:
                    previous = word[pointer]

                elif ord(word[pointer]) < ord(previous):
                    result += 1
                    break

                else:
                    previous = word[pointer]

            pointer += 1

        return result

