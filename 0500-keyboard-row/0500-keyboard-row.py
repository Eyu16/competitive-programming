class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        result = []
        for word in words:
            set_word = set(word.lower())
            if set_word <= row1 or set_word <= row2 or set_word <= row3:
                result.append(word)
        return result
                
        
        