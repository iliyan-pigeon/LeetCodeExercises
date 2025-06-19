class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        result = 0
        current_hours, current_minutes = current.split(":")
        correct_hours, correct_minutes = correct.split(":")

        current_time = int(current_hours) * 60 + int(current_minutes)
        correct_time = int(correct_hours) * 60 + int(correct_minutes)

        difference = correct_time - current_time
        increase_minutes = [60, 15, 5, 1]

        for minutes in increase_minutes:

            operations = difference // minutes
            difference -= operations * minutes
            result += operations

        return result
