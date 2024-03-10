class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_cords = []
        for point in points:
            x_cords.append(point[0])
        x_cords.sort()
        gap = 0
        for i in range(len(x_cords) - 1):
            gap = max(gap, x_cords[i + 1] - x_cords[i])
        return gap
