class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        largest = 0
        while i < len(s):
            subString = s[i:]
            if len(subString) <= largest:
             break
            subStream = ""
            for k in subString:
                if k not in subStream:
                    subStream += k
                else:
                    break
            if len(subStream) > largest:
                largest = len(subStream)
            i += 1
        return largest