class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = date.split("-")

        months = {"01": 0, "02": 31, "03": 59, "04": 90, "05": 120, "06": 151, "07": 181, "08": 212, "09": 243,
                  "10": 273, "11": 304, "12": 334}

        result = int(day) + months[month]

        if int(year) % 400 == 0 or int(year) % 4 == 0 and int(year) % 100 != 0:
            result += 1

        return result
