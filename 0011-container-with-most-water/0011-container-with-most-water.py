class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_val = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_val = max(max_val, area)
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            
        return max_val
