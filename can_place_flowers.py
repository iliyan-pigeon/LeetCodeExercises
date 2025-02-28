# Solution 1
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        possible_plants = 0
        previous = None

        for i in range(len(flowerbed)):
            if (previous is None or previous == 0) and flowerbed[i] == 0:
                if i == len(flowerbed) - 1:
                    possible_plants += 1
                    previous = 1
                elif flowerbed[i + 1] == 0:
                    possible_plants += 1
                    previous = 1
            elif flowerbed[i] == 1:
                previous = 1
            else:
                previous = 0
        if n <= possible_plants:
            return True
        return False


# Solution 2
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        currentflowers = sum(flowerbed)
        flowerbed.insert(0,0)
        flowerbed.append(0) # adding two zeros at the begining and the end will not change the result
        for j in range(1,len(flowerbed)-1):
            if (flowerbed[j] == 0) and (flowerbed[j-1] == 0) and (flowerbed[j+1] == 0):
                flowerbed[j] = 1
        maxflowers = sum(flowerbed)
        return currentflowers+n <= maxflowers
