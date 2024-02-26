class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zero_count = 0
        one_count = 0
        total_zero = nums.count(0)
        total_one = len(nums) - total_zero
        max_val = 0
        res = []
        index_sum_map = {}

        for i in range(len(nums)+ 1):
            if i == 0:
                if nums[i] == 0:
                    zero_count += 1
                    max_val = max(max_val, total_zero)
                else:
                    one_count += 1
                index_sum_map[i] = total_one
                max_val = max(max_val, total_one)
            elif i == len(nums):
                index_sum_map[i] = total_zero
                max_val = max(max_val, total_zero)
            else:
                if nums[i] == 0:
                    sums = zero_count + total_one - one_count
                    zero_count += 1
                    max_val = max(max_val, sums)
                    index_sum_map[i] = sums

                else:
                    sums = zero_count + total_one - one_count
                    one_count += 1
                    max_val = max(max_val, sums)
                    index_sum_map[i] = sums

        for key in index_sum_map:
            if index_sum_map[key] == max_val:
                res.append(key)

        return res




