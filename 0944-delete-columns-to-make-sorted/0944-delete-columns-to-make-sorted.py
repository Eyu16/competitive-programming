class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        counted = 0
        for i in range(len(strs[0])):
            res = []
            for j in range(len(strs)):
                res.append(strs[j][i])
            if res != sorted(res):
                counted += 1

        return counted
