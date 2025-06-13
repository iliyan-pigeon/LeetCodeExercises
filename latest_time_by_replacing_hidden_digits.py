class Solution:
    def maximumTime(self, time: str) -> str:

        for i, v in enumerate(time):
            if v == "?":
                if i == 0:
                    if int(time[i+1]) <= 4:
                        time = time.replace(v, "2", 1)
                    else:
                        time = time.replace(v, "9", 1)
                elif i == 1:
                    if int(time[i-1]) == 2:
                        time = time.replace(v, "4", 1)
                    else:
                        time = time.replace(v, "9", 1)
                elif i == 3:
                    time = time.replace(v, "5", 1)
                elif i == 4:
                    time = time.replace(v, "9", 1)

        return time
