class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringNum = str(x)
        start = 0
        end = len(stringNum)-1
        while start <= end:
            if(stringNum[start] != stringNum[end]):
                return False
            start += 1
            end -= 1
        return True
            
        
    
        