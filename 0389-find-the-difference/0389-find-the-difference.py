class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_t,count_s = Counter(t),Counter(s)
        for count in count_t:
            if count not in count_s:
                return count
            elif count_t[count] > count_s[count]:
                return count
                
            
        
       
        