class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:    
        count = 0
        result = []
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[i] > nums[j]:
                    count += 1;
            result.append(count)
            count = 0
        return result
                
        