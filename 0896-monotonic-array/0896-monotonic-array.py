class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
          if len(nums) == 1:
            return True
          else:
            if nums[0] < nums[-1]:
                for i in range(len(nums)-1):
                    if nums[i+1] - nums[i] < 0:
                        return False
            else:
                for i in range(len(nums)-1):
                    if nums[i+1] - nums[i] > 0:
                        return False
            return True