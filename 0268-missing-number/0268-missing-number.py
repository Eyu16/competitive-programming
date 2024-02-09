class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)+1
        nums = set(nums)
        all_nums = set(range(size))
        return list(nums ^ all_nums)[0]
        