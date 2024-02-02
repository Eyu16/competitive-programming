class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:     
        array = [None] * len(indices)
        for i in range(len(indices)):
            array[indices[i]] = s[i]
        return "".join(array)