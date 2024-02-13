class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        appearance = int(len(nums)/3)
        frequency_map = Counter(nums)
        result = []
        for key in frequency_map:
            if frequency_map[key] > appearance:
                result.append(key)
        return result

        