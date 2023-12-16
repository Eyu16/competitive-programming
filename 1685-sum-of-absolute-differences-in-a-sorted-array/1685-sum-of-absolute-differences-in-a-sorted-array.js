/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getSumAbsoluteDifferences = function(nums) {
    let totalSum = nums.reduce((acc,cur) => acc+cur,0);
    let leftSum = 0;
    let ans = [];
    for(let i = 0 ; i < nums.length ; i++){
        let rightSum = totalSum - nums[i] - leftSum;
        ans.push( i * nums[i] - leftSum + (rightSum - ((nums.length - 1 - i) * nums[i])))
        
            leftSum += nums[i]
    }
    return ans;
};



