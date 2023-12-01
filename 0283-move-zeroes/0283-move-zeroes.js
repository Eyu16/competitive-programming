/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let i = 0;
    let m = 0;
    while(m < nums.length){
        if(nums[m] !== 0 ){
            swap(nums,i,m);
            i++;
        }
        m++;;
        }
};

const swap = function (nums, i, j) {
  const temp = nums[i];
  nums[i] = nums[j];
  nums[j] = temp;
};