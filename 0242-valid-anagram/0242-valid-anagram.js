/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
   let output = true;
  s = s.split("").sort();
  t = t.split("").sort();
  if (t.length !== s.length) return false;
  s.forEach((_, i, s) => {
    if (t[i] !== s[i]) output = false;
  });
  return output;
};