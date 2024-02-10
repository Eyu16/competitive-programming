class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        below = []
        above = []
        middle = []
        for num in nums:
            if num < pivot:
                below.append(num)
            elif num > pivot:
                above.append(num)
            else:
                middle.append(num)

        return below +middle+ above

        