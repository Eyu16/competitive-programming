class Solution:
    def addDigits(self, num: int) -> int:
        digit = list(str(num))
        if len(digit) == 1:
            return num
        sums = 0
        while len(digit) != 1:
            sums = 0
            for i in range(len(digit)):
                sums += int(digit[i])
            digit = list(str(sums))
        return sums
        
        