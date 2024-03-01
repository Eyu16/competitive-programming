class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = []
        loop = int(len(nums) / 2)
        start = 0
        end = -1
        for _ in range(loop):
            res.append(nums[start] + nums[end])
            start += 1
            end -= 1

        return max(res)
