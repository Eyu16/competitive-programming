class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0 
        subStreams = list() 
        while i < len(s): 
            subString = s[i:] 
            subStream = '' 
            for k in subString: 
                if k not in subStream: 
                    subStream += k 
                else: 
                    break 
                subStreams.append(subStream) 
            i += 1 
        maximum = 0 
        for word in subStreams: 
            if len(word) > maximum: 
                maximum = len(word) 
        return maximum