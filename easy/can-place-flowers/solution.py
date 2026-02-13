class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_ok = (i == 0) or (flowerbed[i-1] == 0)
                right_ok = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)

                if left_ok and right_ok:
                    flowerbed[i] = 1
                    count += 1

        return count >= n
