/**
 * @param {number[]} nums
 * @return {number}
 */
var minStartValue = function(nums) {
    // let startValue = 1;
    // let curSum = 0;
    // let minSum = 0;
    // for(let i = 0;i<nums.length;i++){
    //   curSum += nums[i];
    //     minSum = Math.min(minSum,curSum);
    // }
    // return startValue - minSum; 
    let curSum = 0;
    let minSum = 0;
    let startValue = 1;
    for(let i = 0;i<nums.length;i++){
        curSum += nums[i];
        minSum = Math.min(curSum,minSum);
    }
    return startValue - minSum;
};