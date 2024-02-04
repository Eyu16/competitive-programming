class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0
        for char in operations:
            if char == '--X' or char == 'X--' :
                count -= 1
            else:
                count += 1
        return count
        
        