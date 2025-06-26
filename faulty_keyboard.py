class Solution:
    def finalString(self, s: str) -> str:
        final_string = ""

        for ch in s:
            if ch == "i":
                final_string = final_string[::-1]
            else:
                final_string += ch
