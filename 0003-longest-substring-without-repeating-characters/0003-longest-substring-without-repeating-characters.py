class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index_map = {}
        l = 0
        c = 0
        i = 0
        while i < len(s):
            if s[i] in index_map:
                l = max(i - index_map[s[i]], l, c)
                c = 1
                i = index_map[s[i]] + 1
                index_map = {s[i]: i}
            else:
                index_map[s[i]] = i
                c += 1
            i += 1
        return max(l, c)