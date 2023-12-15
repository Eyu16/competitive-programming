/**
 * @param {number} n
 * @return {number}
 */
var pivotInteger = function(n) {
    let totalSum = (n*(n+1))/2;
    let leftSum = 0;
    for(let i = 1; i <= n ; i++){
       totalSum -= i;
        if(totalSum === leftSum)
            return i
        leftSum+=i;
    }
     
    return -1;
};

