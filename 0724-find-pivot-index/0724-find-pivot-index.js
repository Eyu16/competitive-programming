/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    let leftSum = 0;
    let totalSum = nums.reduce((acc,cur)=>acc+cur,0);
    for(let i = 0 ; i < nums.length ; i++){
        totalSum -= nums[i];
        if(leftSum == totalSum)
            return i;
        leftSum += nums[i];
    }
    return -1;
};