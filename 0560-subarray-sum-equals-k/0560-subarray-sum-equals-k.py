class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_map = defaultdict(int)
        cum_sum = 0
        sum_map[0] = 1
        count = 0
        for i in range(len(nums)):
            cum_sum += nums[i]
            if cum_sum - k in sum_map:
                count += sum_map[cum_sum - k]

            sum_map[cum_sum] += 1

        return count
        