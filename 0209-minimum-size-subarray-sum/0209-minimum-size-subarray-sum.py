class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        m_l = float("inf")
        cum_sum = 0
        while i < len(nums) and j < len(nums):
            cum_sum += nums[j]
            if cum_sum >= target:
                m_l = min(m_l, j - i + 1)
                cum_sum -= nums[i]
                i += 1
                cum_sum -= nums[j]
                if j < i:
                    j = i

            else:
                j += 1
        if m_l != float("inf"):
            return min(m_l, j - i + 1)
        return 0
