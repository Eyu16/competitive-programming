class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        frequency_map = {}
        for num in nums:
            if num in frequency_map:
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1
        for num in frequency_map:
            if frequency_map[num] == 1:
                return num
