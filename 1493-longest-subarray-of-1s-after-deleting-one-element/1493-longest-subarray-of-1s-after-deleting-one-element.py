class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = 0
        num_of_zeroes = 1
        while r < len((nums)):
            if nums[r] == 0:
                num_of_zeroes -= 1
            if num_of_zeroes < 0:
                if nums[l] == 0:
                    num_of_zeroes += 1
                l += 1
            r += 1

        return r - l - 1