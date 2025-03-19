from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()

        for i, s in enumerate(senate):
            if s == "R":
                radiant.append(i)
            else:
                dire.append(i)

        senators_count = len(senate)
        while radiant and dire:
            current_radiant = radiant.popleft()
            current_dire = dire.popleft()

            if current_radiant < current_dire:
                radiant.append(current_radiant + senators_count)
            else:
                dire.append(current_dire + senators_count)

        return "Radiant" if radiant else "Dire"
