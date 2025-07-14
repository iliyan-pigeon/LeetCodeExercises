class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"

        for i in range(n-1):
            previous = result[0]
            count = 0
            new_result = ""
            for ch in result:
                if ch == previous:
                    count += 1
                    previous = ch
                else:
                    new_result += f"{count}{previous}"
                    previous = ch
                    count = 1
            new_result += f"{count}{result[-1]}"
            result = new_result

        return result
