var sortedSquares = function(nums) {
  nums.forEach((num, index, array) => {
    array[index] = num * num;
  });

  nums.sort((a, b) => a - b);

  return nums;
};
