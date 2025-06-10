class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan": "1", "Feb": "2", "Mar": "3", "Apr": "4", "May": "5", "Jun": "6", "Jul": "7", "Aug": "8",
                  "Sep": "9", "Oct": "10", "Nov": "11", "Dec": "12"}

        day, month, year = date.split(" ")
        result = [year]

        month = months[month]

        result.append(month)

        day = day[:-2]
        if len(day) == 1:
            day = "0"+day

        result.append(day)

        return "-".join(result)
