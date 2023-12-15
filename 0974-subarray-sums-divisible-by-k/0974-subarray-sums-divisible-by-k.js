var subarraysDivByK = function(nums, k) {
    let count = 0;
    let sumRemainder = 0;
    let remainderMap = new Map();
    remainderMap.set(0,1);
    for(let i = 0 ; i < nums.length ; i++){
        sumRemainder = (sumRemainder + nums[i])%k
        if(sumRemainder < 0)
            sumRemainder += k;
        if(remainderMap.has(sumRemainder)){
            count += remainderMap.get(sumRemainder);
          remainderMap.set(sumRemainder,remainderMap.get(sumRemainder)+1);
        }
        else{
            remainderMap.set(sumRemainder,1);
        }
    }

    return count;
};