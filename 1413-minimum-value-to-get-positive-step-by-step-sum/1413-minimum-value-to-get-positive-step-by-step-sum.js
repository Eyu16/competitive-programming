/**
 * @param {number[]} nums
 * @return {number}
 */
var minStartValue = function(nums) {
    
    let startValue = 1;
    let curSum = 0;
    let minSum = 0;
    for(let i = 0;i<nums.length;i++){
      curSum += nums[i];
        minSum = Math.min(minSum,curSum);
    }
    return startValue - minSum;
    
};