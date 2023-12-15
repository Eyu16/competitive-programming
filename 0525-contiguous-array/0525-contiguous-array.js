/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxLength = function(nums) {
    const sumMap = new Map();
    let maxLen = 0;
    let sum = 0;

    for (let i = 0; i < nums.length; i++) {
        // Treat 0 as -1 and 1 as 1
        sum += nums[i] === 0 ? -1 : 1;

        // If the sum is 0, the subarray from the beginning has equal 0s and 1s
        if (sum === 0) {
            maxLen = i + 1;
        } else if (sumMap.has(sum)) {
            // If the current sum has been encountered before, update maxLen
            maxLen = Math.max(maxLen, i - sumMap.get(sum));
        } else {
            // Store the first occurrence of the sum
            sumMap.set(sum, i);
        }
    }

    return maxLen;
};
