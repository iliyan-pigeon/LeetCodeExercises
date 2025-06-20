class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = ""
        current = ""

        for ch in num:
            if not current:
                current += ch
            elif ch == current[0]:
                current += ch
            else:
                current = ch

            if len(current) == 3:
                if result is "":
                    result = current
                    current = ""
                elif int(result) < int(current):
                    result = current
                    current = ""

        return result
