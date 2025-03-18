from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []

        for asteroid in asteroids:
            if not result:
                result.append(asteroid)

            elif asteroid < 0:
                if result[-1] > 0:
                    current = result[-1]
                    while abs(asteroid) > current > 0:
                        result.pop()
                        if result:
                            current = result[-1]
                        elif not result:
                            current = 0
                    if current == abs(asteroid):
                        result.pop()
                    if current <= 0:
                        result.append(asteroid)
                elif result[-1] < 0:
                    result .append(asteroid)
            elif asteroid > 0:
                result.append(asteroid)

        return result
