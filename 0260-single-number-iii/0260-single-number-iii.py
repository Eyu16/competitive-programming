class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        maps = Counter(nums)
        result = []
        for key in maps:
            if maps[key] == 1:
                result.append(key)
        return result
        