/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
var selfDividingNumbers = function(left, right) {
    let array = [];
  for (let i = left; i <= right; i++) {
    let num = i;
    i = String(i);
    if (!i.includes("0"))
      for (let k = 0; k < i.length; k++) {
        let d = +i[k];
        if (num % d !== 0) break;
        if (num % d == 0 && k == i.length - 1) array.push(num);
      }
  }
  return array;
};