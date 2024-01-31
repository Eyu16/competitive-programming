class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0: return True
        if x < 0:
            return False
        else:
            stringNum = ""
            temp = x;
            while temp > 0:
                remainder = temp % 10
                temp = int(temp / 10)
                stringNum += str(remainder)
            return stringNum == str(x)
        
    
        