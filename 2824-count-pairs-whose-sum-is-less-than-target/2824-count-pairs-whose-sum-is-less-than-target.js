/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
// var countPairs = function(nums, target) {
//     let counter = 0;
//     for(let i = 0 ; i < nums.length-1 ; i++){
//         for(let j=i+1; j<nums.length;j++){
//             if( (nums[i] + nums[j]) < target)
//             counter++;
//         }
//     }
    
//     return counter;
// };
var countPairs = function(nums, target) {
//     let counter = 0;
//     let numCount = new Map();

//     for (let num of nums) {
//         let complement = target - num;

//         if (numCount.has(complement)) {
//             counter += numCount.get(complement);
//         }

//         // Update the map with the current number
//         numCount.set(num, (numCount.get(num) || 0) + 1);
//     }

//     return counter;
    let counter = 0
    let l = 0;
    let r = nums.length-1;
    nums.sort((a,b)=>a-b);
    while(l<r){
        if(nums[l]+nums[r] < target){
            counter += (r-l);
            l++;
        }
        else
            r--
    }
    return counter;
};
