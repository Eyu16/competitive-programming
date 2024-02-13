class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        result = []
        for num in nums:
            if num < 0:
                negative.append(num)
            else:
                positive.append(num)

        for i in range(len(positive)):
            result.append(positive[i])
            result.append(negative[i])
        return result


        