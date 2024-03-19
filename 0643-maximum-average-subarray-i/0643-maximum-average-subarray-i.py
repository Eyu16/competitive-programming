class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = 0
        for i in range(0, k):
            sums += nums[i]
        max_sum = sums / k
        i = 0
        j = k
        while j < len(nums):
            sums += (nums[j] - nums[i])
            max_sum = max(max_sum, sums / k)
            i += 1
            j += 1
        return max_sum
