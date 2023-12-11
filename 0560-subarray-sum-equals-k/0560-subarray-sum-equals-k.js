var subarraySum = function (nums, k) {
  // let sum = 0;
  // let count = 0;
  // let sumCountMap = new Map();
  // sumCountMap.set(0, 1);
  // for (let i = 0; i < nums.length; i++) {
  //   sum += nums[i];
  //   if (sumCountMap.has(sum - k)) {
  //     count += sumCountMap.get(sum - k);
  //   }
  //   if(sumCountMap.has(sum)){
  //     sumCountMap.set(sum,sumCountMap.get(sum)+1);
  //   }
  //   else{
  //     sumCountMap.set(sum,1);
  //   }
  // }
  // return count;
    let count = 0;
    let sum = 0; 
    let sumCountMap = new Map();
    sumCountMap.set(0,1);
    for(let i = 0 ; i < nums.length; i++){
        sum += nums[i];
        if(sumCountMap.has(sum-k)){
            count += sumCountMap.get(sum-k);
        }
        if(sumCountMap.has(sum)){
            sumCountMap.set(sum,sumCountMap.get(sum)+1)
        }
        else{
            sumCountMap.set(sum,1)
        }
    }
    return count;
};