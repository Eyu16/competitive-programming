/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    x = String(x);
    let str = '';
    for(let i = x.length - 1; i>=0; i--){
        str += x[i];
    }

    return x === str ? true:false;
};