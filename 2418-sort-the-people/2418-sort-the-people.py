class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # height_map = {}
        # for i in range(len(names)):
        #     height_map[heights[i]] = names[i]
        n = len(names)
        for i in range(len(heights)):
            for j in range(n - 1):
                if heights[j] < heights[j + 1]:
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]
                    names[j], names[j + 1] = names[j + 1], names[j]
            n -= 1
                    
                    
        return names
        
                    
                
                
        