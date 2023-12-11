var subarraysDivByK = function(nums, k) {
    let count = 0;
    let remainder = 0;
    let remainderMap = new Map();
    remainderMap.set(0, 1);

    for (let i = 0; i < nums.length; i++) {
      remainder = (remainder + nums[i]) % k;
        if (remainder < 0) {
            // Handle negative remainders
            remainder += k;
        }
        if (remainderMap.has(remainder)) {
            count += remainderMap.get(remainder);
            remainderMap.set(remainder, remainderMap.get(remainder) + 1);
        }

       else {
            remainderMap.set(remainder, 1);
        }
    }

    return count;
    // let count = 0;
    // let remainder = 0;
    // let remainderMap = new Map();
    // remainderMap.set(0,1);
    // for(let i = 0; i < nums.length;i++){
    //     remainder = (remainder + nums[i]) % k;
    //     if(remainder < 0){
    //         remainder += k;
    //         if(remainderMap.has(remainder)){
    //             count += remainderMap.get(remainder);
    //             remainderMap.set(remainder,remainderMap.get(remainder)+1);
    //         }
    //         else{
    //             remainderMap.set(remainder,1);
    //         }
    //     }
    // }
    // return count;
};
