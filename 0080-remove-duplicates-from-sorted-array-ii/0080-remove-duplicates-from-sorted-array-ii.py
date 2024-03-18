class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        indexs = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
                if count > 2:
                    indexs.append(i)
            else:
                count = 1

        for ind in indexs:
            nums[ind] = float("inf")

        nums.sort()
        print(nums)
        return len(nums) - len(indexs)
