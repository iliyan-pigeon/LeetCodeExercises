class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        if name[0] != typed[0]:
            return False

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
                    elif typed[t_index] != typed[t_index-1]:
                        return False
            if not valid:
                return False

            t_index += 1

        while t_index <= len(typed)-1:
            if typed[t_index] != name[-1]:
                return False
            t_index += 1

        return True
