class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        middle = 0
        end = len(nums) - 1
        while middle <= end:
            if nums[middle] == 2:
                nums[middle], nums[end] = nums[end], nums[middle]
                end -= 1
            elif nums[middle] == 1:
                middle += 1
            else:
                nums[start], nums[middle] = nums[middle], nums[start]
                start += 1
                middle += 1

        return nums
        # m = 0;
        # l = 0;
        # r = len(nums) - 1;
        # while m <= r:
        #     if nums[m] == 2:
        #         nums[m], nums[r] = nums[r], nums[m]
        #         r -= 1
        #     elif nums[m] == 1:
        #         m += 1
        #     else:
        #         nums[l], nums[m] = nums[m], nums[l]
        #         m += 1
        #         l += 1
        # return nums
    