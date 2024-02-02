class Solution:
    def rotateString(self, s: str, goal: str) -> bool: 
        # if len(s) != len(goal):
        #     return False
        # s = s + s
        # if goal in s :
        #     return True
        # return False
        return (len(s) == len(goal) and goal in s + s)
    

        