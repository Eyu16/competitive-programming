class Solution:
    def sortString(self, s: str) -> str:
        result = ""
        s = list(s)
        s.sort()
        total_char = len(s)
        while len(result) < total_char:
            result_small = ""
            result_large = ""
            result_small =self.pick_smallest(s, result_small)
            result_large = self.pick_largest(s, result_large)
            print(result_small)
            print(result_large)
            result += (result_small + result_large)
        return result
        
        
    def pick_smallest(self,s, result):
        for i in range(len(s)):
            char = s[i]
            if len(result) > 0:
                if char > result[-1]:
                    result += char
            else:
                result += char
        for char in result:
            s.remove(char)
        return result


    def pick_largest(self,s, result):
        for i in range(len(s)-1, -1, -1):
            char = s[i]
            if len(result) > 0:
                if char < result[-1]:
                    result += char
            else:
                result += char
        for char in result:
            s.remove(char)
        return result
   

     
            
        
        