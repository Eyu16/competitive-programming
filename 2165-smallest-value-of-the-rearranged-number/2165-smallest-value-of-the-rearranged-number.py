class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            num = sorted(str(num))
            if num[0] == '0':
                i = 1
                while num[i] == '0' and i < len(num):
                    i += 1
                num[0], num[i] = num[i], num[0]
            return int("".join(num))
        else:
            num = num * -1
            num = reversed(sorted(str(num)))
            return -1 * int("".join(num))
