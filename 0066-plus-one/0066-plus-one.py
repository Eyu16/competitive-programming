class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        char_digit = "".join(list(map(str, digits)))
        res = []
        char_digit = str(int(char_digit) + 1)
        for char in char_digit:
            res.append(int(char))
        return res
        