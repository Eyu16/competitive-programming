class Solution:
    def firstUniqChar(self, s: str) -> int:
        frquency_count = Counter(s)            
        for i in range(len(s)):
            if frquency_count[s[i]] == 1:
                return i
        return -1
        