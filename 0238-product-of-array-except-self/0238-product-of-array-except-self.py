class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix_sum = []
        p_p = 1
        sufix_sum = []
        for num in nums:
            p_p *=(num)
            prefix_sum.append(p_p)
        p_p = 1
        for k in range(len(nums) - 1, -1, -1):
            p_p *= nums[k]
            sufix_sum.append(p_p)
        i = 0
        j = len(nums) - 2
        res = []
        while i < len(nums):
            if i == 0:
                res.append(sufix_sum[j])
            elif i == len(nums) - 1:
                res.append(prefix_sum[i - 1])
            else:
                res.append(prefix_sum[i - 1] * sufix_sum[j])
            i += 1
            j -= 1
        return res
