class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        result_one = ""
        result_two = ""
        for string in word1:
            result_one += string
        for string in word2:
            result_two += string

        return result_one == result_two
        