class Solution:
    def areNumbersAscending(self, s: str) -> bool:

        s = s.split(" ")
        last_number = 0

        for token in s:
            if token.isnumeric():
                if last_number >= int(token):
                    return False

                last_number = int(token)

        return True
