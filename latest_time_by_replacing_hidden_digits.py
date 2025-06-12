from random import randint


class Solution:
    def maximumTime(self, time: str) -> str:

        for i, v in enumerate(time):
            if v == "?":
                if i == 0:
                    time = time.replace(v, str(randint(0, 2)), 1)
                elif i == 1:
                    time = time.replace(v, str(randint(0, 3)), 1)
                elif i == 3:
                    time = time.replace(v, str(randint(0, 5)), 1)
                elif i == 4:
                    time = time.replace(v, str(randint(0, 9)), 1)

        return time
