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
    let i = 0;
    let j = 0;

    while (i < word1.length && j < word2.length) {
        merged += word1[i] + word2[j];
        i++;
        j++;
    }

    // Append the remaining characters from the non-empty string
    merged += word1.slice(i) + word2.slice(j);

    return merged;
};

