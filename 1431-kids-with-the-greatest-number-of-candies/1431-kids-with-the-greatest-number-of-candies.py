class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maxnum = max(candies)
        for i in range(len(candies)):
            added = candies[i] + extraCandies
            if added >= maxnum:
                result.append(True)
            else:
                result.append(False)
        return result