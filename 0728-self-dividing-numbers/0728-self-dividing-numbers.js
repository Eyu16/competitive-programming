/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
var selfDividingNumbers = function(left, right) {
    let arr = [];
    for(let i = left ; i<=right ; i++){
        if(i%10 == 0) continue;
       let strNum  = i;
        strNum = String(strNum);
        for(let k = 0; k < strNum.length ; k++){
            if(i%(+strNum[k]) !== 0) break;
            if(i%(+strNum[k]) == 0 && k == strNum.length-1) arr.push(i)
        }
    }
    return arr;
};