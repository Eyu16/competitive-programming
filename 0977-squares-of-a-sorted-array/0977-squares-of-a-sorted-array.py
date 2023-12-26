class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = []
        i = 0
        j = len(nums) - 1
        while(i <= j):
            if(abs(nums[i] ) > abs(nums[j])):
                answer.append(nums[i] * nums[i])
                i += 1
            else:
                answer.append(nums[j] * nums[j])
                j -= 1
            
        return answer[::-1]
        
      
        