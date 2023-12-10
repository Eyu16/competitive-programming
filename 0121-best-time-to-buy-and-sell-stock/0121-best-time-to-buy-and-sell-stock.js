/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    if (prices.length < 2) {
        return 0; // Cannot make a profit with less than two prices
    }

    let minPrice = prices[0];
    let maxProfit = 0;

    for (let i = 1; i < prices.length; i++) {
        // Update the minimum price
        minPrice = Math.min(minPrice, prices[i]);

        // Update the maximum profit based on the difference between the current price and the minimum price
        maxProfit = Math.max(maxProfit, prices[i] - minPrice);
    }

    return maxProfit;
};


