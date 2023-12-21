/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    let i = 0;
    let sortedSquared = []
    let j= nums.length - 1
    let x = j
    while(i <= j){
        if(Math.abs(nums[i])>Math.abs(nums[j])){
        sortedSquared[x] = nums[i] * nums[i];
            i++;
        }
        else{
            sortedSquared[x] = nums[j] * nums[j];
            j--;
        }
        x--;
    }
    return sortedSquared;
};