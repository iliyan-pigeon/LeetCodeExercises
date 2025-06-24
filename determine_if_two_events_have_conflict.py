from typing import List


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        event1_start, event1_end = event1
        event2_start, event2_end = event2

        event1_start_hour = int(event1_start.split(":")[0])
        event1_start_minute = int(event1_start.split(":")[1])

        event1_end_hour = int(event1_end.split(":")[0])
        event1_end_minute = int(event1_end.split(":")[1])

        event2_start_hour = int(event2_start.split(":")[0])
        event2_start_minute = int(event2_start.split(":")[1])

        event2_end_hour = int(event2_end.split(":")[0])
        event2_end_minute = int(event2_end.split(":")[1])

        event_one_start = event1_start_hour * 60 + event1_start_minute
        event_one_end = event1_end_hour * 60 + event1_end_minute

        event_two_start = event2_start_hour * 60 + event2_start_minute
        event_two_end = event2_end_hour * 60 + event2_end_minute

        if event_one_start <= event_two_start <= event_one_end:
            return True
        if event_one_start <= event_two_end <= event_one_end:
            return True
        if event_one_start >= event_two_start and event_one_end <= event_two_end:
            return True
        if event_two_start >= event_one_start and event_two_end <= event_one_end:
            return True

        return False
