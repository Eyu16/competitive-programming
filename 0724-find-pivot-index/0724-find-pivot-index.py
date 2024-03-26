class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            total_sum -= nums[i]
            if total_sum == left_sum:
                return i
            else:
                left_sum += nums[i]
        return -1
        