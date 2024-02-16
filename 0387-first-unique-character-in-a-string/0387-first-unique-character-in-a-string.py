class Solution:
    def firstUniqChar(self, s: str) -> int:
        frquency_count = Counter(s)
        map_index = defaultdict(int)
        for i in range(len(s)):
            map_index[s[i]] = i
            
        for char in s:
            if frquency_count[char] == 1:
                return map_index[char]
        return -1
        