class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        cumulative = 0
        j = 1
        k = len(piles) - 1
        piles.sort(reverse=True)
        while j < k:
            cumulative += piles[j]
            j += 2
            k -= 1
        return cumulative