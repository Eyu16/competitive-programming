class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:    
        sorted_num = sorted(nums)
        index_map = defaultdict(list)
        for i in range(len(sorted_num)):
            index_map[sorted_num[i]].append(i)

        res = []
        for num in nums:
            res.append(index_map[num][0] - 0)
        return res
        