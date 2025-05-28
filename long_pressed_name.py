class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        valid = True
        t_index = 0
        for i, v in enumerate(name):

            if t_index == len(typed):
                return False

            if v != typed[t_index]:
                valid = False
                while t_index < len(typed)-1:
                    t_index += 1
                    if v == typed[t_index]:
                        valid = True
                        break
            if not valid:
                return False

            t_index += 1

        if t_index <= len(typed)-1:
            return False

        return True
