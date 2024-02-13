class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        result_one = "".join(word1)
        result_two = "".join(word2)
        return result_one == result_two
        