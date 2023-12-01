/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
let temp;
    for(let i = 0 ; i < nums.length ; i++){
        for(let j = i+1 ;j>=0;j--){
            if(nums[j-1]>nums[j]){
                temp = nums[j-1];
                nums[j-1] = nums[j];
                nums[j] = temp
            }
            else{
                break;
            }
        }
    }
    return nums;
};