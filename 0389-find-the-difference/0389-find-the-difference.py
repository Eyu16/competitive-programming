class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        s = ''.join(s)
        t = ''.join(t)
        start = 0
        while start < len(s):
            if s[start] != t[start]:
                return t[start]
            start += 1
        return t[-1]
                
            
        
       
        