class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        result = ""
        max_check = len(strs[0])
        for word in strs:
            max_check = len(word) if max_check > len(word) else max_check
        for i in range(max_check):
            if strs[0][i] == strs[-1][i]:
                result += strs[0][i]
            else:
                break
        return result
            
        