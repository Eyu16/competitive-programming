class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            return 0
        counter = 0
        sorted_nums = sorted(list(set(nums)))
        f_m = Counter(nums)
        i = len(sorted_nums) - 1
        j = i - 1
        while j >= 0 and i > 0:
            counter += f_m[sorted_nums[i]]
            f_m[sorted_nums[j]] += f_m[sorted_nums[i]]
            i -= 1
            j -= 1
        return counter
        
        