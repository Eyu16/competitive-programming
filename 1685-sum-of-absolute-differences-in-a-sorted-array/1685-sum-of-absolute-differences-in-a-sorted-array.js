/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getSumAbsoluteDifferences = function(nums) {
let cumulativeSum = [0];
    let ans = [];
    for(let i = 0 ; i < nums.length ; i++){
        cumulativeSum[i+1] = cumulativeSum[i] + nums[i];
    }
    cumulativeSum = cumulativeSum.slice(1);
    for(i = 0 ; i < nums.length ; i++){
        if( i === 0 || i === nums.length - 1 ){
            ans.push(Math.abs(cumulativeSum[nums.length-1] -( nums[i] * nums.length)))
        }
        else{
            let leftSum = cumulativeSum[i-1];
            let rightSum = cumulativeSum[nums.length - 1] - cumulativeSum[i];
            let sum = Math.abs(leftSum - (i * nums[i])) + Math.abs(rightSum - ((nums.length - 1 - i) * nums[i] ))
            ans.push(sum);
        }
    }
    return ans;
};



