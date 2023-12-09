/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) {
    let numCount = {};
    let counter = 0;
    for(let num of nums){
      if(numCount[num]){
          counter += numCount[num];
      } 
     numCount[num] = (numCount[num]||0)+1;
    }
return counter;
};