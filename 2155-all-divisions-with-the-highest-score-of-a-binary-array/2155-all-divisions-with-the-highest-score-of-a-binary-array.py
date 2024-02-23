class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zero_count = 0
        one_count = 0
        max_val = 0
        res = []
        index_count_map = {}
        index_sum_map = {}

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
                index_count_map[i] = [zero_count, one_count]
            else:
                one_count += 1
                index_count_map[i] = [zero_count, one_count]

        for i in range(len(nums) + 1):
            if i == 0:
                sums = index_count_map[len(nums) - 1][1]
                max_val = max(max_val, sums)
                index_sum_map[i] = sums
            elif i == len(nums):
                sums = index_count_map[i - 1][0]
                max_val = max(max_val, sums)
                index_sum_map[i] = sums
            else:
                sums = index_count_map[i-1][0] + index_count_map[len(nums)-1][1] - index_count_map[i - 1][1]
                max_val = max(max_val, sums)
                index_sum_map[i] = sums

        for key in index_sum_map:
            if index_sum_map[key] == max_val:
                res.append(key)
                
        return res



