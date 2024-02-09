class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        map_fr = Counter(nums)
        result = []
        for key in map_fr:
            if map_fr[key] == 2:
                result.append(key)
                
        return result
            
        