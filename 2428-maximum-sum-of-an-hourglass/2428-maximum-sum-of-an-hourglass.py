class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_s = 0
        rows = len(grid)
        columns = len(grid[0])
        for i in range(rows - 2):
            for j in range(columns - 2):
                max_s = max(sumOfPattern(grid, [i, j]), max_s)

        return max_s


def sumOfPattern(grid, index):
    return grid[index[0]][index[1]] + grid[index[0]][index[1] + 1] + grid[index[0]][index[1] + 2] + grid[
        index[0] + 1][index[1] + 1] + grid[index[0] + 2][index[1]] + grid[index[0] + 2][index[1] + 1] + grid[
        index[0] + 2][index[1] + 2]

        