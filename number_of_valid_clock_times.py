class Solution:
    def countTime(self, time: str) -> int:
        valid_times = 1
        hours, minutes = time.split(":")

        if hours[0] == "?" and hours[1] == "?":
            valid_times *= 24
        elif hours[0] == "?":
            if int(hours[1]) < 4:
                valid_times *= 3
            else:
                valid_times *= 2
        elif hours[1] == "?":
            if int(hours[0]) == 2:
                valid_times *= 4
            else:
                valid_times *= 10

        if minutes[0] == "?" and minutes[1] == "?":
            valid_times *= 60
        elif minutes[0] == "?":
            valid_times *= 6
        elif minutes[1] == "?":
            valid_times *= 10

        return valid_times
