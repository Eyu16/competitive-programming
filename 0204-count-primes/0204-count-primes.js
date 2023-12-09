/**
 * @param {number} n
 * @return {number}
 */
var countPrimes = function (n) {
let primes = new Array(n).fill('true');
    for(let i = 2 ; i*i<n;i++){
        if(primes[i])
            for(let j = i; j*i<n;j++){
                primes[j*i] = false;
            }
    }
    let counter = 0;
    for(let i = 2;i<n;i++){
        if(primes[i])
            counter++;
    }
    return counter;
};

