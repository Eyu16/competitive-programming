class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set(nums)
        nums_copy = list(num_set)
        return not(len(nums_copy) == len(nums))
        