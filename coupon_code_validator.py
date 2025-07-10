from typing import List


class Solution:
    def validateCoupons(self, code: List[str], business: List[str], isActive: List[bool]) -> List[str]:
        grouped = {}

        for i in range(len(code)):
            if not code[i]:
                continue

            for ch in code[i]:
                if not ch.isalnum() and ch != "_":
                    break
            else:
                if business[i] in ["electronics", "grocery", "pharmacy", "restaurant"] and isActive[i] is True:
                    if business[i] not in grouped:
                        grouped[business[i]] = []
                    grouped[business[i]].append(code[i])

        result = []

        for business in sorted(grouped):
            result.extend(sorted(grouped[business]))

        return result
