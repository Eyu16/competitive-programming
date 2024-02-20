class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [num for num in range(1, n + 1)]
        start = 0
        while len(arr) > 1:
            remove = (start + k - 1) % len(arr)
            arr.pop(remove)
            start = remove
        return arr[0]
            
            
        
        