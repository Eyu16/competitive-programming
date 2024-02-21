class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        if sorted_nums == nums:
            return 0
        dec = []
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                dec = nums[i + 1:]
                if dec[-1] < nums[0] and sorted(dec) == dec:
                    return len(dec)
                else:
                    return -1
