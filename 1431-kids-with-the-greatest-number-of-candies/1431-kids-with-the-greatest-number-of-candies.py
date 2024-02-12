class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for i in range(len(candies)):
            added = candies[i] + extraCandies
            if added >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result