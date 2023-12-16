/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    // const occurMap = new Map();
    // for(let i = 0 ; i < nums.length ; i++){
    //     if(occurMap.has(nums[i])){
    //         occurMap.set(nums[i],occurMap.get(nums[i])+1);
    //         if(occurMap.get(nums[i]) > 1){
    //             return true;
    //         }
    //     }
    //     else{
    //         occurMap.set(nums[i],1);
    //     } 
    // }
    const numsSet = new Set();
    for(let i = 0 ; i < nums.length ; i++){
        if(numsSet.has(nums[i]))
            return true;
        numsSet.add(nums[i]);
    }
    return false;
};