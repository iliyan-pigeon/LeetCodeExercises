class Solution:
    def clearDigits(self, s: str) -> str:

        while not s.isalpha():
            list_s = list(s)
            deleted = False
            for i, ch in enumerate(list_s):
                if ch.isnumeric():
                    alpha_index = i

                    while alpha_index > 0:
                        alpha_index -= 1
                        if list_s[alpha_index].isalpha():
                            list_s.pop(i)
                            list_s.pop(alpha_index)
                            deleted = True
                            break

                    if deleted:
                        break
            else:
                break

            s = "".join(list_s)

            if not list_s:
                break

        return s
