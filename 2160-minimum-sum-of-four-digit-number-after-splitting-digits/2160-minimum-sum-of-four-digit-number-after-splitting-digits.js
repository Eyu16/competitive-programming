/**
 * @param {number} num
 * @return {number}
 */
var minimumSum = function(num) {
    let array = [];
    let digits = String(num).split('');
    digits = digits.sort((a,b)=>a-b);
    array.push(digits[0]+digits[2]);
    array.push(digits[1]+digits[3]);
    return Number(array[0])+Number(array[1]);
};