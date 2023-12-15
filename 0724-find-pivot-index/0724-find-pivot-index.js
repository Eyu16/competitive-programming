/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    let totalSum = nums.reduce((acc,cur)=>acc+cur,0);
    let leftSum = 0;
    for(let i = 0 ; i < nums.length ; i++){
        totalSum -= nums[i];
        if(totalSum === leftSum)
            return i;
            leftSum += nums[i]
    }
    return -1;
    
};