/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function (s) {
  s = s.split(" ");
  let ans = new Array(s.length).fill(0);
  for (let i = 0; i < s.length; i++) {
    let index = +s[i].slice(-1) - 1;
    ans[index] = s[i].slice(0, -1);
  }
  return ans.join(" ");
};