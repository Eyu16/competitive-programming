var findMaxLength = function(nums) {
    let maxLength = 0;
    let sum = 0;
    let sumMap = new Map();
    sumMap.set(0,-1);
    for(let i = 0 ; i < nums.length ; i++){
        sum += nums[i] === 0? -1:1;
        if(sumMap.has(sum)){
            maxLength = Math.max(maxLength,i-sumMap.get(sum));
        }
        else{
            sumMap.set(sum,i);
        }
    }
    return maxLength;
}

