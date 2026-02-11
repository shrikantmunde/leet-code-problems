class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result =[]
        max =0
        for i in candies:
            if i > max:
                max = i
        for i in candies:
            if i + extraCandies >= max:
                result.append(True)
            else:
                result.append(False)
        return result
    
    # Ideal Solution
    # class Solution(object):
    # def kidsWithCandies(self, candies, extraCandies):
    #     # Find out the greatest number of candies among all the kids.
    #     maxCandies = max(candies)
    #     # For each kid, check if they will have greatest number of candies
    #     # among all the kids.
    #     result = []
    #     for i in range(len(candies)):            
    #         result.append(candies[i] + extraCandies >= maxCandies)
    #     return result