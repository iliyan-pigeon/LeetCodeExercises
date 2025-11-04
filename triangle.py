from typing import List


class Solution:
    def minimumTotal(self, triangle: [List[List[int]]]) -> int:

        for i, row in enumerate(triangle):
            if i == len(triangle)-1:
                return min(row)

            new_row = [[] for _ in range(len(triangle[i+1]))]

            for index, number in enumerate(row):
                current_number = number + triangle[i+1][index]
                new_row[index].append(current_number)

                if index != len(triangle[i+1])-1:
                    current_number = number + triangle[i+1][index+1]
                    new_row[index+1].append(current_number)

            triangle[i+1] = [min(i) for i in new_row]


# Solution 2
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]
    