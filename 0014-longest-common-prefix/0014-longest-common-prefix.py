class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        result = ""
        max_check = len(strs[0])
        for i in range(max_check):
            if strs[0][i] == strs[-1][i]:
                result += strs[0][i]
            else:
                break
        return result
            
        