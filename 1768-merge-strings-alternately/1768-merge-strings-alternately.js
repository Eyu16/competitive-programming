// /**
//  * @param {string} word1
//  * @param {string} word2
//  * @return {string}
//  */
// var mergeAlternately = function(word1, word2) {
//     let str='';
//     size = word1.length > word2.length?word1.length:word2.length;
//     for(let i = 0 ; i<size ; i++){
//         if(word1[i])
//      str+=word1[i];
//      if(word2[i])
//      str+=word2[i];
//     }
//     return str;
// };
/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
 let merged = '';
 let j = 0;
 let k = 0;
    while(j<word1.length && k<word2.length){
        merged += word1[j]+word2[k];
        j++;
        k++;
    }
    merged += word1.slice(j)+word2.slice(k);
    return merged;
};

