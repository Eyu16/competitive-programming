class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = ""
        for i in range(n):
            num = start + 2 * i
            if result == "":
                result = num
            else:
                result ^= num

        return result
        