class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        largest = ''
        while i < len(s):
            subString = s[i:]
            subStream = ''
            for k in subString:
                if k not in subStream:
                    subStream += k
                else:
                    break
            if len(subStream) > len(largest):
                largest = subStream
            i += 1
        return len(largest)