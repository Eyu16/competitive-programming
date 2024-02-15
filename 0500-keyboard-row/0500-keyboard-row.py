class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        string = "qwertyuiopasdfghjklzxcvbnm"
        map_index = {value: i for i, value in enumerate(string)}
        result = []
        for word in words:
            word_set = set(word.lower())
            l = len(word_set)
            temp1 = set()
            temp2 = set()
            temp3 = set()
            for char in word.lower():
                if map_index[char] <= 9:
                    temp1.add(char)
                elif 10 <= map_index[char] <= 18:
                    temp2.add(char)
                else:
                    temp3.add(char)
            if l == len(temp1) or l == len(temp2) or l == len(temp3):
                result.append(word)

        return result
        