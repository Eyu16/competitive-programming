class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            temp = []
            while num > 0:
                r = num%10
                num = int(num / 10)
                temp.append(r)
            res.extend(temp[::-1])
        return res
            
       
        