// /**
//  * @param {number[]} nums
//  * @return {void} Do not return anything, modify nums in-place instead.
//  */
// var sortColors = function(nums) {
// // let temp;
// //     for(let i = 0 ; i < nums.length ; i++){
// //         for(let j = i+1 ;j>=0;j--){
// //             if(nums[j-1]>nums[j]){
// //                 temp = nums[j-1];
// //                 nums[j-1] = nums[j];
// //                 nums[j] = temp
// //             }
// //             else{
// //                 break;
// //             }
// //         }
// //     }
// //     return nums;
//     let temp;
//     let i = 0;
//     let k = 0;
//     let j = nums.length - 1;
//     let ans = [];
//      while(i<j){
//          if(nums[i] === 2){
//              if(ans[j+1] == 1){
//                  ans[j+1] = 2;
//                  ans[j] = 1;
//                  i++;
//                  j--;
//              }
//          }
//        else if(nums[i] === 1){
//            ans[j]=1;
//            j--;
//            i++;
//        }
//            else{
//                ans[k] = 0
//                i++;
//                k++;
//            }
//      }
//     return ans;
// };
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    let i = 0; // Pointer for 0s
    let j = 0; // Pointer for 1s
    let k = nums.length - 1; // Pointer for 2s

    while (j <= k) {
        if (nums[j] === 0) {
            swap(nums, i, j);
            i++;
            j++;
        } else if (nums[j] === 1) {
            j++;
        } else {
            swap(nums, j, k);
            k--;
        }
    }
};

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
// var sortColors = function(nums) {
//     let i = 0; // Pointer for 0s
//     let j = 0; // Pointer for 1s
//     let k = nums.length - 1; // Pointer for 2s

//     while (j <= k) {
//         if (nums[j] === 0) {
//             swap(nums, i, j);
//             i++;
//             j++;
//         } else if (nums[j] === 1) {
//             j++;
//         } else {
//             swap(nums, j, k);
//             k--;
//         }
//     }
// };

// function swap(nums, i, j) {
//     const temp = nums[i];
//     nums[i] = nums[j];
//     nums[j] = temp;
// }
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
//     let low = 0;         // Pointer for 0s
//     let high = nums.length - 1;  // Pointer for 2s
//     let i = 0;           // Current position

//     while (i <= high) {
//         if (nums[i] === 0) {
//             swap(nums, i, low);
//             i++;
//             low++;
//         } else if (nums[i] === 2) {
//             swap(nums, i, high);
//             high--;
//         } else {
//             i++;
//         }
//     }
    let m = 0;
    let j = 0;
    let k = nums.length - 1;
    while(m <= k){
        if(nums[m] == 2){
            swap(nums,m,k);
            k--;
        }
           else if(nums[m] == 1)
               m++;
            else{
                swap(nums,j,m)
                j++;
                m++;
            }
    }
};

function swap(nums, i, j) {
    const temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
}

