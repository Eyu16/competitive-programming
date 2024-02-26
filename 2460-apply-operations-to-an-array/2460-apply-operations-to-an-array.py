class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        k = 0
        j = 0
        while j < len(nums):
            if nums[j] == 0:
                j += 1
            else:
                nums[k], nums[j] = nums[j], nums[k]
                k += 1
                j += 1
        return nums
