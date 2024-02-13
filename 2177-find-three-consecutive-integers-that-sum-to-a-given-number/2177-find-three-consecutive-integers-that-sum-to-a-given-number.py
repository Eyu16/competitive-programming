class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num == 0:
            return [-1, 0, 1]
        elif(num%3):
            return []
        else:
            n = int(1 + num/3)
            return [n-2,n-1,n]
        