/**
 * @param {number[]} nums
 */
var NumArray = function(nums) {
    this.cumulativeSum = [0];
    
    for (let i = 0; i < nums.length; i++) {
        this.cumulativeSum[i + 1] = this.cumulativeSum[i] + nums[i];
    }
};

/** 
 * @param {number} left 
 * @param {number} right
 * @return {number}
 */
NumArray.prototype.sumRange = function(left, right) {
    return this.cumulativeSum[right + 1] - this.cumulativeSum[left];
};

/** 
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * var param_1 = obj.sumRange(left,right)
 */
