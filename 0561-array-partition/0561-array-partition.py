class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
            nums.sort()
            ssum = 0
            for i in range(0, len(nums) - 1, 2):
                ssum += nums[i]
            return(ssum)
        