// /**
//  * @param {number} left
//  * @param {number} right
//  * @return {number[]}
//  */
var selfDividingNumbers = function(left, right) {
    let arr = [];
    // for(let i = left ; i<=right ; i++){
    //     if(i%10 == 0) continue;
    //    let strNum  = i;
    //     strNum = String(strNum);
    //     for(let k = 0; k < strNum.length ; k++){
    //         if(i%(+strNum[k]) !== 0) break;
    //         if(i%(+strNum[k]) == 0 && k == strNum.length-1) arr.push(i)
    //     }
    // }
    for(let i = left ; i <= right ; i++){
        if(i%10 == 0) continue;
        let isSelefDividing = true;
        let num = i;
        while(num > 0){
            const digit = num%10;
            if(i%digit !== 0){
                isSelefDividing = false;
                break;
            }
            num = Math.floor(num/10);
        }
        if(isSelefDividing) arr.push(i);
    }
    return arr;
};
/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
// var selfDividingNumbers = function(left, right) {
//     let arr = [];
    
//     for (let i = left; i <= right; i++) {
//         if (i % 10 === 0) continue; // Skip numbers ending in 0
        
//         let isSelfDividing = true;
//         let num = i;
        
//         while (num > 0) {
//             const digit = num % 10;
            
//             if (i % digit !== 0) {
//                 isSelfDividing = false;
//                 break;
//             }
            
//             num = Math.floor(num / 10); // Move to the next digit
//         }
        
//         if (isSelfDividing) {
//             arr.push(i);
//         }
//     }
    
//     return arr;
// };
var selfDividingNumbers = function (left, right) {
  let arr = [];
  for(let i = left ; i<=right;i++){
    if(i%10 == 0) continue;
    let num = i;
    let isSelefD = true;
    while(num>0){
      let digit =  num%10;
      if(i%digit !== 0){
        isSelefD = false;
        break;
      }
      num = Math.floor(num/10);
    }
if(isSelefD) 
arr.push(i);
  }
return arr;
};
