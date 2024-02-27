class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ind_map = defaultdict(list)
        for i in range(len(nums)):
            ind_map[nums[i]].append(i)

        return ind_map[target]
        