/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
  let max = Math.max(...nums)+1;
    let smaller = new Array(max).fill(0);
//     for(let i = 0; i<nums.length;i++){
//         smaller[nums[i]]++;
//     }
//     for(let i = 1 ; i < smaller.length ; i++){
//         smaller[i] += smaller[i-1]
       
//     }
//     for(let i = 0 ; i<nums.length ; i++){
//         let position = nums[i];
//         if(position === 0) nums[i] = 0;
//         else{
//             nums[i] = smaller[position-1];
            
//         }
//     }
    for(let i = 0 ; i < nums.length ; i++){
        smaller[nums[i]]++;
    }
    for(let i = 1 ; i < smaller.length ; i++){
        smaller[i] += smaller[i-1];
    }
    for(let i = 0 ; i < nums.length ; i++){
        let pos = nums[i];
        if(pos === 0) nums[i] = 0;
        else{
            nums[i] = smaller[pos-1];
        }
    }
    return nums;
};