from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        result = []

        for i in range(len(img)):
            row = []

            for j in range(len(img[i])):
                new_number = img[i][j]
                delimiter = 1

                if i-1 >= 0:
                    new_number += img[i-1][j]
                    delimiter += 1

                    if j-1 >= 0:
                        new_number += img[i-1][j-1]
                        delimiter += 1

                    if j+1 < len(img[i]):
                        new_number += img[i-1][j+1]
                        delimiter += 1

                if i+1 < len(img):
                    new_number += img[i+1][j]
                    delimiter += 1

                    if j-1 >= 0:
                        new_number += img[i+1][j-1]
                        delimiter += 1

                    if j+1 < len(img[i]):
                        new_number += img[i+1][j+1]
                        delimiter += 1

                if j-1 >= 0:
                    new_number += img[i][j-1]
                    delimiter += 1

                if j+1 < len(img[i]):
                    new_number += img[i][j+1]
                    delimiter += 1

                new_number = new_number // delimiter
                row.append(new_number)

            result.append(row)

        return result
      
