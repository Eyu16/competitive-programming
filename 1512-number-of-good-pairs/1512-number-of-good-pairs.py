class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = {}
        count = 0
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        for key in counter:
            count += counter[key] * (counter[key] - 1) / 2

        return int(count)

        
        