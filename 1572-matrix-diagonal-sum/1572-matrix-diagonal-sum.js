/**
 * @param {number[][]} mat
 * @return {number}
 */
var diagonalSum = function(mat) {
    if(!mat.length > 1) return mat.flat().at(0);
    let n = mat.length;
    let sum = 0; 
    for(let i = 0 ; i < n  ; i++){
        sum += mat[i][i];
        sum += mat[n-1-i][i];
    }
    if(n % 2 == 1){
        let mid = Math.floor(n/2);
        sum -= mat[mid][mid];
    }
  
return sum;
};