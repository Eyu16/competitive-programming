var subarraysDivByK = function(nums, k) {
    let count = 0;
    let sum = 0;
    let remainderMap = new Map();
    remainderMap.set(0, 1);

    for (let i = 0; i < nums.length; i++) {
        sum = (sum + nums[i]) % k;
        if (sum < 0) {
            // Handle negative remainders
            sum += k;
        }
        if (remainderMap.has(sum)) {
            count += remainderMap.get(sum);
            remainderMap.set(sum, remainderMap.get(sum) + 1);
        }

       else {
            remainderMap.set(sum, 1);
        }
    }

    return count;
};
