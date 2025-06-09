import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        return (datetime.date(*[int(i) for i in date1.split("-")]) - datetime.date(*[int(i) for i in date2.split("-")])).days
