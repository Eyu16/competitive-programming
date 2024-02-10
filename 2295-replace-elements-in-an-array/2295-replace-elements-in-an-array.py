class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index_map = {value: index for index, value in enumerate(nums)}
        for i in range(len(operations)):
            nums[index_map[operations[i][0]]] = operations[i][1]
            index_map[operations[i][1]] = index_map[operations[i][0]]
        return nums
