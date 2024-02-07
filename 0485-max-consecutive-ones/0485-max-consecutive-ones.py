class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        result = []
        for num in nums:
            if num == 1:
                count += 1
            else:
                result.append(count)
                # [2,
                count = 0
        else:
            result.append(count)
        return sorted(result)[-1]
        