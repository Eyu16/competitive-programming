class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = 0
        result = []
        for num in nums:
            sums += num
            result.append(sums)
        return result
