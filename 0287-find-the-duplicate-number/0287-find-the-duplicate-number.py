class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        r = max(nums) + 1
        counts = [0] * r
        for i in range(len(nums)):
            counts[nums[i]] += 1
        temp = 0
        for i in range(len(counts)):
            for _ in range(counts[i]):
                nums[temp] = i
                temp += 1
        i = 0
        j = 1

        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                j += 1
            else:
                return nums[i]
