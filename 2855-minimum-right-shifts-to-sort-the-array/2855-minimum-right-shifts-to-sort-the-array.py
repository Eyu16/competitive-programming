class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        start_index = 0
        count = 0
        for i in range(len(nums) - 1):
            if count > 1:
                return -1
            if nums[i + 1] < nums[i]:
                start_index = i + 1
                count += 1
        else:
            if count == 0:
                return 0
            if count == 2:
                return -1
            else:
                if nums[0] > nums[-1]:
                    return len(nums) - start_index
                else:
                    return -1

