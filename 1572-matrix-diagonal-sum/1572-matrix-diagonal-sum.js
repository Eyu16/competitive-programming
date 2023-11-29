/**
 * @param {number[][]} mat
 * @return {number}
 */
var diagonalSum = function(mat) {
    if(!mat.length > 1) return mat.flat().at(0);
    let length = mat.length;
    mat = mat.flat();
    let sum = 0;
        for(let i = 0, j = length - 1 ; i < mat.length , j < mat.length ; i += (length+1), j += (length - 1)){
             if(i > mat.length) break;
            sum += mat[i];
         if( i!== j)
             sum += mat[j];
            
        }
    return sum;
};