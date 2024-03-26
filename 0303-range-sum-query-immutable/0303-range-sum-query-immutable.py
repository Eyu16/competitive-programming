class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.cum_sum = 0
        self.prefix_sum = []
        for num in self.nums:
            self.cum_sum += num
            self.prefix_sum.append(self.cum_sum)
        
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.prefix_sum[right] - 0
        else:
            return self.prefix_sum[right] - self.prefix_sum[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)