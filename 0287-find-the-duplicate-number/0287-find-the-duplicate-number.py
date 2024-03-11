class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        j = 1
        nums.sort()
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                j += 1
            else:
                return nums[i]
        
        