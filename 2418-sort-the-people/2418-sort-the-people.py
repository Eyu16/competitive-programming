class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
#         n = len(names)
#         for i in range(len(heights)):
#             for j in range(n - 1):
#                 if heights[j] < heights[j + 1]:
#                     heights[j], heights[j + 1] = heights[j + 1], heights[j]
#                     names[j], names[j + 1] = names[j + 1], names[j]
#             n -= 1    
            
            
            
        # for i in range(len(heights) - 1):
        #     min_index = i
        #     for j in range(i + 1, len(heights)):
        #         if heights[min_index] < heights[j]:
        #             min_index = j
        #     heights[i],heights[min_index] = heights[min_index], heights[i]
        #     names[i], names[min_index] = names[min_index], names[i]
            
        for i in range(len(heights) - 1):
            for j in range(i + 1, 0, -1):
                if heights[j] > heights[j - 1]:
                    heights[j], heights[j - 1] = heights[j - 1], heights[j]
                    names[j], names[j - 1] = names[j - 1], names[j]
                    
        return names



            
            
        return names
        
                    
                
                
        