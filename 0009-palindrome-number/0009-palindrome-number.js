/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if(x<0) return false;
let strNum = String(x);
let start = 0;
let end = strNum.length-1;
    while(start<end){{
        if(strNum[start] !== strNum[end]){
            return false;
        }
        start++;
        end--;
    }
        
    }
    return true;
};