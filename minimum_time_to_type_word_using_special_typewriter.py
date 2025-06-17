class Solution:
    def minTimeToType(self, word: str) -> int:
        time = 0
        position = 97
        current_position = 97

        for ch in word:
            current_time_one = 1

            while ch != chr(current_position):
                current_position += 1
                current_time_one += 1

                if current_position > 122:
                    current_position = 97

            current_time_two = 1
            current_position = position

            while ch != chr(current_position):
                current_position -= 1
                current_time_two += 1

                if current_position < 97:
                    current_position = 122

            position = current_position

            time += min(current_time_one, current_time_two)

        return time
