class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 0
        s = ""
        if len(chars) == 1:
            return len(chars)
        while i < len(chars) - 1:
            if chars[i] == chars[i + 1]:
                i += 1
            else:
                s += chars[i]
                count = i - j + 1
                if count > 1:
                    s += str(count)
                i += 1
                j = i

        if chars[i] == chars[i - 1]:
            count = i - j + 1
            s += chars[i]
            if count > 1:
                s += str(count)
        else:
            s += chars[i]
        for i in range(len(s)):
            chars[i] = s[i]

        return len(s)

