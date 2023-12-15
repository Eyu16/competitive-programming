/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let num1 = [...nums];
    num1.sort((a,b)=>a-b);
    console.log(nums)
    let i = 0 ;
    let j = num1.length - 1;
    while(i < j){
        if(num1[i]+num1[j] === target)
            return [nums.indexOf(num1[i]),nums.lastIndexOf(num1[j])];
        else if(num1[i]+num1[j] > target)
            j--;
        else i++;
    }
    
};