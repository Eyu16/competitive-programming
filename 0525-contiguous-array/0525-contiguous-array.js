var findMaxLength = function(nums) {
    const sumMap = new Map();
    let maxLen = 0;
    let sum = 0;

    // Initialize sumMap with an entry for 0 and its index as -1
    sumMap.set(0, -1);

    for (let i = 0; i < nums.length; i++) {
        sum += nums[i] === 0 ? -1 : 1;

        if (sumMap.has(sum)) {
            maxLen = Math.max(maxLen, i - sumMap.get(sum));
        } else {
            sumMap.set(sum, i);
        }
    }

    return maxLen;
};
