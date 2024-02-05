class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        frequency_map = {}
        for num in nums:
            if num in frequency_map:
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1
        for key in frequency_map:
            if frequency_map[key] == 1:
                return key
        