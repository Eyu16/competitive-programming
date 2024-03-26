class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        r = 0
        p = 1
        count = 0
        while r < len(nums) and l <= r:
            p *= nums[r]
            while p >= k and l < len(nums):
                p = int(p / nums[l])
                l += 1
            count += (r - l + 1)
            r += 1

        if count >= 0:
            return count
        else:
            return 0
        