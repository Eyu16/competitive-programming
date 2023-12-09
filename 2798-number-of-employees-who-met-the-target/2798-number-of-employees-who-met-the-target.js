/**
 * @param {number[]} hours
 * @param {number} target
 * @return {number}
 */
var numberOfEmployeesWhoMetTarget = function(hours, target) {
let counter = 0;
hours.forEach(hour=>{if(hour >= target)
counter++;
})
// return counter;
// for(let i = 0 ; i < hours.length ; i++){
//     if(hours[i] >= target) counter++
// }
return counter;
};