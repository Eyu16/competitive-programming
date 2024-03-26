class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix_sum = []
        cum_sum = 0
        for num in nums:
            cum_sum += num
            prefix_sum.append(cum_sum)
            
        return prefix_sum
        