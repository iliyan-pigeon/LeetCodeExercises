from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        result = 0

        for item in items:
            if ruleKey == "type" and ruleValue == item[0]:
                result += 1
            elif ruleKey == "color" and ruleValue == item[1]:
                result += 1
            elif ruleKey == "name" and ruleValue == item[2]:
                result += 1

        return result
