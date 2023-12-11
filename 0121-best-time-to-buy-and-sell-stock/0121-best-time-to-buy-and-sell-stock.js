/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    // let minPrice = prices[0];
    let maxProfit = 0;
    let left = 0;
    let right = 1;
    let profit = 0;
    // for(let i = 1 ; i<prices.length;i++){
    //     minPrice = Math.min(minPrice,prices[i]);
    //     maxProfit = Math.max(maxProfit,prices[i]-minPrice);
    // }
    while(right <prices.length){
        if(prices[left]<prices[right]){
        profit = prices[right] - prices[left];
        maxProfit = Math.max(profit,maxProfit);
        }
        else{
            left = right;
        }
        right++;
    }
    return maxProfit;
};